from statistics import mode
from djongo import models
from django import forms

"""class AImages(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    image =  models.ImageField(upload_to='images/')
    icon = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
"""
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('title',)

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    proj_link = models.URLField(null=True, blank=True)  # needed for itchio widget
    proj_embed_link = models.URLField(null=True, blank=True)  # needed for itchio widget
    proj_playable_link = models.URLField(null=True, blank=True)  # webGL playable version of itchio widget
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('created',)

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project.title

    def get_first_image():
        pass
    def get_project_images():
        pass
    
class ContactForm(forms.Form):
    person_name = forms.CharField(max_length=50)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class DocTag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class UploadDocument(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(DocTag, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class About_detail(models.Model):
    greeting = models.TextField()  # Short introduction
    detail = models.TextField()  # Motivation letter
    image = models.ImageField(upload_to='images/')