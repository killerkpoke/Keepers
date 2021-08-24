from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('myWorks/', views.mywork, name='works'),
    path('contact/', views.contact, name='contact'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)