from django.db import models
from django import forms

class MultiImage(models.Model):
    name = models.CharField(max_length=100, default='test')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def default(self):
        return self.images.filter(default=True).first()
    def project_thumbnail(self):
        return self.images.filter(default=False).first()
    def thumbnails(self):
        return self.images.filter(default=False).all()

class ImageProject(models.Model):
    name = models.CharField(max_length=100)
    img =  models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(MultiImage, related_name='images',on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    cat_album = models.OneToOneField(MultiImage, related_name='codel',on_delete=models.CASCADE)
    
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
    proj_link = models.URLField(null=True, blank=True)  # needed for itchio widget
    proj_embed_link = models.URLField(null=True, blank=True)  # needed for itchio widget
    proj_playable_link = models.URLField(null=True, blank=True)  # webGL playable version of itchio widget
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    proj_album = models.OneToOneField(MultiImage, related_name='podel',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['created']


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
        ordering = ['name']

    def get_cv():
        cv = UploadDocument.objects.get(name="CV").file
        return cv
