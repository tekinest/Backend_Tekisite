from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.signals import post_save
from django.conf import settings
from .fields import AddressField
import random
import string
import uuid
import pycountry

# from api.v0.schools.models import School

country_choices = [(country.alpha_3, country.name) for country in pycountry.countries]


# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def _create_fulluser(
        self, email, username, first_name, last_name, password, **extra_fields
    ):
        if not email:
            raise ValueError("The given email must be set")
        if not username:
            raise ValueError("The given username must be set")
        if not first_name:
            raise ValueError("The given first_name must be set")
        if not last_name:
            raise ValueError("The given last_name must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, first_name, last_name, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self._create_fulluser(
            email, username, first_name, last_name, password, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email + " " + self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name


# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_by", blank=True, null=True
    )
    students = models.ManyToManyField(User, related_name="students", blank=True)
    teachers = models.ManyToManyField(User, related_name="teachers", blank=True)
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    logo = models.ImageField(upload_to="tekisite/schools/logos/", blank=True)
    cover = models.ImageField(upload_to="tekisite/schools/covers/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ("-created_at",)  # newest to oldest

    def __str__(self):
        return f"{self.name}"


class UserProfileManager(models.Manager):
    pass


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
]


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile",
        blank=False,
        null=False,
    )
    gender = models.CharField(
        max_length=255, choices=GENDER_CHOICES, blank=True, null=True
    )
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="tekisite/profile_pics", blank=True, null=True)
    address = AddressField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=True)
    school = models.OneToOneField(
        School,
        on_delete=models.CASCADE,
        related_name="school_profile",
        blank=True,
        null=True,
    )
    school_info = models.CharField(max_length=255, blank=True, null=True)
    school_address = AddressField(max_length=255, blank=True, null=True)
    school_logo = models.ImageField(upload_to="tekisite/school_logo", blank=True, null=True)
    parent = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="parent_profile",
        blank=True,
        null=True,
    )
    nationality = models.CharField(choices=country_choices, max_length=3, default="NGA")
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_tek_admin = models.BooleanField(default=False)
    is_tek_staff = models.BooleanField(default=False)
    is_tek_manager = models.BooleanField(default=False)

    objects = UserProfileManager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username