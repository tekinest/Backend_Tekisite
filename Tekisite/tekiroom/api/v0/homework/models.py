
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django import forms
from django.utils import timezone



User = get_user_model()
ASSIGNEMENT_TYPES = (
    ('homework', 'Homework'),
    ('quiz', 'Quiz'),
    ('project', 'Project'),
    ('challenge', 'Challenge'),
    ('exam', 'Exam'),
    ('misc', 'Miscellaneous'),
)

# Create your models here.
class Assignment(models.Model):
    assignment_type = models.CharField(max_length=999, choices=ASSIGNEMENT_TYPES, default='misc')
    title = models.CharField(max_length=200)
    description = models.TextField()
    attachment = models.FileField(upload_to='tekiroom/assignments/', blank=True, null=True)
    due_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assignments')
    students = models.ManyToManyField(User, related_name='assignments', through='Grade')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    meta_tags = models.JSONField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.is_published = True
        self.publish_date = timezone.now()
        self.save()
    def publish_assignment(self):
        if self.publish_date <= timezone.now():
            self.is_published = True
            self.save()



class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student.username}'s grade for {self.assignment.title} "
    # method that set the grade based on the score
    def set_grade(self):
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 80:
            self.grade = 'B'
        elif self.score >= 70:
            self.grade = 'C'
        elif self.score >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
        self.save()
        return self.grade
    

class Submission(models.Model):
    ALLOWED_EXTENSIONS = ['pdf', 'doc', 'docx', 'zip']
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    attachment_one = models.FileField(upload_to='tekiroom/submissions/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
    attachment_two = models.FileField(upload_to='tekiroom/submissions/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
    attachment_three = models.FileField(upload_to='tekiroom/submissions/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_late = models.BooleanField(default=False, editable=False)
 



    def __str__(self):
        return f"{self.student.username}'s submission for {self.assignment.title} on {self.submitted_at.ctime()}"
    
    def is_submission_late(self):
        if self.submitted_at > self.assignment.due_date:
            self.is_late = True
            self.save()
            return self.is_late
        else:
            self.is_late = False
            self.save()
            return self.is_late
    def get_grade(self):
        return self.grade.grade
