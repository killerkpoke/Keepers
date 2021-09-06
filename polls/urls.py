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
    path('my-stacks/<slug:slug>/', views.my_project, name='project'),
    path('my-stacks/<slug:slug>/<int:id>', views.project_detail, name='project_detail'),    
    path('contact/', views.contact, name='contact'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)