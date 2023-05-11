# Create your views here.
from rest_framework import viewsets , permissions, status,generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response 



from django.http import Http404 
from .models import  User, UserProfile
from .serializers import UserSerializer , UserProfileSerializer , NormalUserRegistrationSerializer, SuperUserRegistrationSerializer
from .permissions import IsOwnerOrReadOnly

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    

class NormalUserRegistrationAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = NormalUserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class SuperUserRegistrationAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = SuperUserRegistrationSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
