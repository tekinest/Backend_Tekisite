# Create your views here.
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, UserProfile
from .permissions import IsOwnerOrReadOnly
from .serializers import (NormalUserRegistrationSerializer,
                          SuperUserRegistrationSerializer,
                          UserProfileSerializer, UserSerializer)


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def list(self, request):
        # Retrieve the authenticated user from the token
        authenticated_user = request.user

        # Filter the queryset to retrieve the specific user based on the authenticated user
        queryset = User.objects.filter(pk=authenticated_user.pk)

        if not queryset.exists():
            return Response("User not found.", status=404)

        user = queryset.first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Retrieve the authenticated user from the token
        authenticated_user = request.user

        # Filter the queryset to retrieve the specific user based on the authenticated user
        queryset = User.objects.filter(pk=authenticated_user.pk)

        if not queryset.exists():
            return Response("User not found.", status=404)

        user = queryset.first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving profiles.
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def list(self, request):
        # Retrieve the authenticated user from the token
        authenticated_user = request.user

        # Filter the queryset to retrieve the specific user based on the authenticated user
        queryset = UserProfile.objects.filter(user=authenticated_user)

        if not queryset.exists():
            return Response("Userprofile not found.", status=404)

        profile = queryset.first()
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Retrieve the authenticated user from the token
        authenticated_user = request.user

        # Filter the queryset to retrieve the specific user based on the authenticated user
        queryset = UserProfile.objects.filter(user=authenticated_user)

        if not queryset.exists():
            return Response("Profile not found.", status=404)

        profile = queryset.first()
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)


class NormalUserRegistrationAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = NormalUserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SuperUserRegistrationAPIView(generics.CreateAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = SuperUserRegistrationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
