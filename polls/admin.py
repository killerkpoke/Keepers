from django.contrib import admin
from .models import Category, Project


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('URL name', {'fields': ['slug']}),
        ('Upload image', {'fields': ['image']}),
    ]
    list_display = ('title', 'slug', 'image')
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project)


