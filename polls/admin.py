from django.contrib import admin
from .models import About_detail, Category, Project,  DocTag, UploadDocument, ProjectImages

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('URL name', {'fields': ['slug']}),
        ('Image album', {'fields': ['img']}),
    ]
    list_display = ('title', 'slug', 'img')

class UploadDocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Choose a Tag', {'fields': ['tag']}),
        ('Choose a file to upload', {'fields': ['file']}),
    ]
    list_display = ('name', 'tag', 'file', 'created')

class ImagesInline(admin.StackedInline):
    model = ProjectImages
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": (['title']),}),
        (None, {"fields": (['description']),}),
        ("Project embeded links", {"fields": (['proj_link']),}),
        (None, {"fields": (['proj_embed_link']),}),
        (None, {"fields": (['proj_playable_link']),}),
        ("Slug field", {"fields": (['slug']),}),
        ("Category type", {"fields": (['category']),}),
        ("Project icon image ", {"fields": (['images']),}),
        
    )
    inlines = [ImagesInline]

    class Meta:
        model = Project

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(DocTag)
admin.site.register(UploadDocument, UploadDocumentAdmin)
admin.site.register(About_detail)


