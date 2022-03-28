from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery-home'),
    # path('photo/<str:pk>/', views.gallery, name='photo'),

]
