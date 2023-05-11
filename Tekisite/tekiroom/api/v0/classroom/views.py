from rest_framework import viewsets, permissions
from .models import Classroom
from .serializers import ClassroomSerializer

class ClassroomView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer