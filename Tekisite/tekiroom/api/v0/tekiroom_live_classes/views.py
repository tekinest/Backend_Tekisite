from rest_framework import viewsets , permissions
from .models import TekiroomLiveClass
from .serializers import TekiroomLiveClassSerializer



class TekiroomLiveClassView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TekiroomLiveClass.objects.all()
    serializer_class = TekiroomLiveClassSerializer
    
