from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('resume/', views.resume, name='resume'),
]
