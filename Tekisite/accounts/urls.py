# from django.conf.urls import urls
from django.urls import include, re_path, path
from .views import UserViewSet, UserProfileView, NormalUserRegistrationAPIView, SuperUserRegistrationAPIView, UserProfileViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename='user'),
router.register(r"profiles", UserProfileViewSet, basename='profile'),
urlpatterns = [
    path("", include(router.urls)),
    path('create-normal-user/', NormalUserRegistrationAPIView.as_view(), name='create_normal_user'),
    path('create-super-user/', SuperUserRegistrationAPIView.as_view(), name='create_super_user'),
]
