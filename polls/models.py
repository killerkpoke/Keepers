from statistics import mode
from djongo import models
from django import forms

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
    images = models.ImageField(upload_to='images/')
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
    greeting = models.TextField(null=True, blank=True)  # Short introduction
    detail = models.TextField(null=True, blank=True)  # Motivation letter
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(null=True, blank=True)
    mobile = models.TextField()
    linkedin = models.TextField(null=True, blank=True) 
    github = models.TextField(null=True, blank=True)