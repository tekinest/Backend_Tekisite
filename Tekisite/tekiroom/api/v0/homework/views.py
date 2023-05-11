from rest_framework import viewsets, permissions
from .models import Assignment, Grade, Submission
from .serializers import AssignmentSerializer, GradeSerializer, SubmissionSerializer
# Create your views here.


class AssignmentView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class GradeView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class SubmissionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer