from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()

# Create your models here.

class Achievement(models.Model):
    ACHIEVEMENT_TYPES = (
        ('COURSE_COMPLETED', 'Course Completed'),
        ('HIGH_SCORE', 'High Score'),
        ('MILESTONE_REACHED', 'Milestone Reached'),
        ('COMMUNITY_PARTICIPATION', 'Community Participation'),
        ('SKILL_LEARNED', 'Skill Learned'),
        ('CHALLENGE_COMPLETED', 'Challenge Completed'),
        ('CERTIFICATION_EARNED', 'Certification Earned'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    achievement_type = models.CharField(max_length=999, choices=ACHIEVEMENT_TYPES, default='misc')

    def __str__(self):
        return self.title

class Reward(models.Model):
    REWARD_TYPES = (
        ('certificate', 'Certificate'),
        ('medal', 'Medal'),
        ('trophy', 'Trophy'),
        ('prize', 'Prize'),
        ('misc', 'Miscellaneous'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    reward_icon = models.ImageField(upload_to='reward_images', blank=True, null=True, default='reward_images/default.png')

    def __str__(self):
        return self.title
class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    rewards = models.ForeignKey(Reward, on_delete=models.CASCADE, blank=True, null=True)
    progress = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_achieved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user.username} earned {self.achievement.title} on {self.updated_at.ctime()}"

class UserReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_achived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} earned {self.reward.title} on {self.updated_at.ctime()}"