from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Photo, Location

# DUMMY DATA
# photos = [
   
#     'https://images.pexels.com/photos/3912838/pexels-photo-3912838.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#     'https://images.pexels.com/photos/62623/wing-plane-flying-airplane-62623.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#     'https://images.pexels.com/photos/11341064/pexels-photo-11341064.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#     'https://images.pexels.com/photos/735338/pexels-photo-735338.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load',
#     'https://images.pexels.com/photos/33129/popcorn-movie-party-entertainment.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 
#     'https://images.pexels.com/photos/2398356/pexels-photo-2398356.jpeg?auto=compress&cs=tinysrgb&w=1600' ,
    
#     'https://images.pexels.com/photos/5011647/pexels-photo-5011647.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
#     'https://images.pexels.com/photos/1421903/pexels-photo-1421903.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
#     'https://images.pexels.com/photos/1612353/pexels-photo-1612353.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',]

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    # image = Photo.objects.get(id=pk)
    context = {
        'categories': categories,
        'photos': photos,
        # 'image': image
    }
    return render(request, 'gallery/home.html', context)


def addPhoto(request):
    context = {
        'photos': photos
    }
    return render(request, 'gallery/add.html', context)

