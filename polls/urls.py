from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'polls'
urlpatterns = [
    path('', views.index),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('my-stacks/', views.my_stack, name='works'),
    path('my-stacks/<slug:category_slug>/', views.my_project, name='project'),
    path('my-stacks/<slug:category_slug>/<slug:project_slug>/', views.project_detail, name='project_detail'),    
    path('contact/', views.contact, name='contact'),
    path('post-json/', views.post_json, name='post-json'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)