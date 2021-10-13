from django.contrib import admin
from .models import Category, Project, MultiImage, ImageProject


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('URL name', {'fields': ['slug']}),
        ('Image album', {'fields': ['cat_album']}),
    ]
    list_display = ('title', 'slug', 'cat_album')
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project)
admin.site.register(ImageProject)
admin.site.register(MultiImage)


