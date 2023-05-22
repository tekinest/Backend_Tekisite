
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