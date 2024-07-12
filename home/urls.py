from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),

]
