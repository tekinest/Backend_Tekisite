from django.urls import include, path, re_path
from .views import AchievementView, RewardView, UserAchievementView, UserRewardView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'achievements', AchievementView),
router.register(r'rewards', RewardView),
router.register(r'userachievements', UserAchievementView),
router.register(r'userrewards', UserRewardView),

urlpatterns = [
    re_path(r"/", include(router.urls)),
]