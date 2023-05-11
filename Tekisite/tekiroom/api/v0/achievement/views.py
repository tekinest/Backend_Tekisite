from rest_framework import viewsets, permissions
from .models import Achievement, Reward, UserAchievement, UserReward
from .serializers import AchievementSerializer, RewardSerializer, UserAchievementSerializer, UserRewardSerializer

# Create your views here.

class AchievementView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class RewardView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class UserAchievementView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

class UserRewardView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserReward.objects.all()
    serializer_class = UserRewardSerializer