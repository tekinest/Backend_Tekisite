import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django import forms

class AddressField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 200)
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        # Add custom validation here, such as checking for valid characters
        # or formatting the address
        if not re.match(r'^[\w\s\-\.\,]+$', value):
            raise ValidationError('Address can only contain letters, numbers, spaces, and these characters: - . ,')

    def formfield(self, **kwargs):
        defaults = {'widget': forms.Textarea}
        defaults.update(kwargs)
        return super().formfield(**defaults)
