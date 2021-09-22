from django.db import models
from django import forms



class MultiImage(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

class ImageProject(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(MultiImage, on_delete=models.CASCADE)
    img =  models.ImageField(upload_to='images/', null=True)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)

class Category(MultiImage):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    #cat_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('title',)
        
    def get_category_list():
        cat = Category.objects.all()
        return cat

class Project(MultiImage):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    #proj_image = models.ImageField(upload_to='images/', null=True)
    proj_link = models.URLField()
    proj_embed_link = models.URLField()
    proj_playable_link = models.URLField(null=True, blank=True)
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
    
    