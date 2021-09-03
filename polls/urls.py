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
    #path('myWorks/<str:slug>/', views.mywork, name='works'),
    
    path('contact/', views.contact, name='contact'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)