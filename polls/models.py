from django.db import models
from django import forms

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/images', null=True)
    file = models.FileField(upload_to='static/uploaded')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created',)

class ContactForm(forms.Form):
    person_name = forms.CharField(max_length=50)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    