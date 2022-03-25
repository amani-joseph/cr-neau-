from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery-home'),
    path('add/', views.addPhoto, name='add'),
]
