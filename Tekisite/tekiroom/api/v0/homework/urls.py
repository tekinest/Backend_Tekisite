from django.urls import include, path, re_path
from .views import AssignmentView, GradeView, SubmissionView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', AssignmentView),
router.register(r'grades', GradeView),
router.register(r'submissions', SubmissionView),

urlpatterns = [
    re_path(r'/', include(router.urls)),
]