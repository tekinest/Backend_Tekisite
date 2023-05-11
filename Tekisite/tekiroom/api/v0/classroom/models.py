from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.
User = get_user_model()
# list of platform choices
PLATFORM_CHOICES = [
    ('tekiroom', 'Tekiroom'),
    ('google_classroom', 'Google Classroom'),
    ('youtube', 'Youtube'),
    ('zoom', 'Zoom'),
    ('google_meet', 'Google Meet'),
    ('microsoft_teams', 'Microsoft Teams'),
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('twitch', 'Twitch'),
    ('discord', 'Discord'),
    ('skype', 'Skype'),
    ('vimeo', 'Vimeo'),
    ('webex', 'Webex'),
    ('other', 'Other')
]

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    classroom_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=False)
    invite_code = models.CharField(max_length=5, unique=True)
    slug = models.SlugField(unique=True)
    platform = models.CharField(max_length=255, choices=PLATFORM_CHOICES)
    platform_url = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teachers = models.ManyToManyField(User, related_name='classrooms_taught')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {str(self.classroom_code)[:5]} at {self.platform_url}"
     
