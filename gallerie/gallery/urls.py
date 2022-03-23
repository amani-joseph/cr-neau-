from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='gallery-home'),
    # path('about/', views.about, name='blog-about'),
]
