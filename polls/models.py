from django.db import models
import datetime
from django.utils import timezone
from django import forms

class Works(models.Model):
    named = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.named

class ContactForm(forms.Form):
    person_name = forms.CharField(max_length=50)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    