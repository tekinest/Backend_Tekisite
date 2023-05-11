from django.urls import include, re_path
from .views import ClassroomView

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r"classroom", ClassroomView)


urlpatterns = [
    re_path(r"/" ,include(router.urls))
]
