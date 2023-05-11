from django.urls import include, path, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'course', views.CourseView),


urlpatterns = [
    re_path(r'/', include(router.urls)),
]