from django.contrib import admin
from .models import About_detail, Category, Project, MultiImage, ImageProject, DocTag, UploadDocument


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('URL name', {'fields': ['slug']}),
        ('Image album', {'fields': ['cat_album']}),
    ]
    list_display = ('title', 'slug', 'cat_album')

class UploadDocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Choose a Tag', {'fields': ['tag']}),
        ('Choose a file to upload', {'fields': ['file']}),
    ]
    list_display = ('name', 'tag', 'file', 'created')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project)
admin.site.register(ImageProject)
admin.site.register(MultiImage)
admin.site.register(DocTag)
admin.site.register(UploadDocument, UploadDocumentAdmin)
admin.site.register(About_detail)


