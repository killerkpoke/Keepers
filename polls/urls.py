from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('program/', views.index, name='program'),
    path('drum/', views.index, name='drum'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]