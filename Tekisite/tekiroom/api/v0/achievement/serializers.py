from rest_framework import serializers
from .models import Achievement, Reward, UserAchievement, UserReward

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('__all__')

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('__all__')

class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAchievement
        fields = ('__all__')

class UserRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReward
        fields = ('__all__')