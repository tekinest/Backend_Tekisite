from rest_framework import serializers, permissions
from .models import User, UserProfile, School


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True},}
        permission_classes = (permissions.IsAuthenticated,)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        permissions = (permissions.IsAuthenticated,)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        permissions = (permissions.IsAuthenticated,)
        
class NormalUserRegistrationSerializer(UserSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects._create_fulluser(
            validated_data["email"],
            validated_data["username"],
            validated_data["first_name"],
            validated_data["last_name"],
            validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields =("__all__")

class SuperUserRegistrationSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        user = User.objects.create_superuser(
            validated_data["email"],
            validated_data["username"],
            validated_data["first_name"],
            validated_data["last_name"],
            validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("email", "username", "password", "first_name", "last_name","is_staff","is_superuser","is_active",)
