from rest_framework import serializers
from .models import Assignment, Grade, Submission

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('__all__')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('__all__')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('__all__')