from django.urls import include, re_path
from .views import TekiroomLiveClassView

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", TekiroomLiveClassView)


urlpatterns = [
    re_path(r"/" ,include(router.urls))
]