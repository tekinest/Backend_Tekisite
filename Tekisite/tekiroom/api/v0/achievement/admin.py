from django.contrib import admin

# Register your models here.

from .models import Achievement, Reward,   UserAchievement, UserReward

admin.site.register(Achievement)
admin.site.register(Reward)
admin.site.register(UserAchievement)
admin.site.register(UserReward)
