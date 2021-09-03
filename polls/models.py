from django.db import models
from django import forms
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    cat_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('title',)
        
    def get_category_list():
        cat = Category.objects.all()
        return cat
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    proj_image = models.ImageField(upload_to='images/', null=True)
    file = models.FileField(upload_to='uploaded/')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['created']

class ContactForm(forms.Form):
    person_name = forms.CharField(max_length=50)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    