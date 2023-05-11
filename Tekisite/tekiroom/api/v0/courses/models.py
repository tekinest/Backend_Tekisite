from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db import models

User = get_user_model()


class Course(models.Model):
    DEPARTMENT_CHOICES = [
        ("FE", "Frontend Engineering"),
        ("BE", "Backend Engineering"),
        ("FS", "Fullstack Engineering"),
        ("DS", "Data Science"),
        ("GT", "General Technology"),
    ]
    COURSES_CHOICES = [
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("JAVASCRIPT", "JAVASCRIPT"),
        ("TYPESCRIPT", "TYPESCRIPT"),
        ("FIGMA", "FIGMA"),
        ("UI", "UI"),
        ("UX", "UX"),
        ("PYTHON", "PYTHON"),
        ("DJANGO", "DJANGO"),
        ("REACT", "REACT"),
        ("NODE", "NODE"),
        ("MONGODB", "MONGODB"),
        ("MYSQL", "MYSQL"),
        ("GIT", "GIT"),
        ("GITHUB", "GITHUB"),
        ("AWS", "AWS"),
        ("DOCKER", "DOCKER"),
        ("KUBERNETES", "KUBERNETES"),
        ("LINUX", "LINUX"),
        ("BASH", "BASH"),
        ("SHELL", "SHELL"),
        ("C", "C"),
        ("OTHER", "OTHER"),
    ]
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    instructor = models.ManyToManyField(User, related_name="Course_instructor")
    course_choice = models.CharField(max_length=20, choices=COURSES_CHOICES)
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    credit_hours = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course_name} in  {self.course_choice} in {self.department}"

    def mark_completed(self):
        self.is_completed = True
        self.save()

    def mark_uncompleted(self):
        self.is_completed = False
        self.save()

    def is_completed(self):
        return self.is_completed
