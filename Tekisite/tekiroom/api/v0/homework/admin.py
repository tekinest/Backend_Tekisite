from django.contrib import admin

# Register your models here.

from .models import Assignment, Grade, Submission

admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Submission)
# admin.site.register(MyAttachment)


