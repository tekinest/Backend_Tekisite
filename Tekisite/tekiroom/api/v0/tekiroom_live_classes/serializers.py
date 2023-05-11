from rest_framework import serializers
from .models import TekiroomLiveClass


class TekiroomLiveClassSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TekiroomLiveClass
        fields = ('__all__')