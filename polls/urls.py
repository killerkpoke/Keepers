from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'polls'
urlpatterns = [
    path('', views.index),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('myWorks/', views.mywork, name='works'),
    path('myWorks/<slug:slug>/', views.myproject, name='project'),
    path('myWorks/<slug:slug>/<int:id>', views.project_detail, name='project_detail'),    
    path('contact/', views.contact, name='contact'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)