from django.shortcuts import render
from django.http import HttpResponse

# DUMMY DATA
photos = ['https://images.pexels.com/photos/5011647/pexels-photo-5011647.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260','https://images.pexels.com/photos/1421903/pexels-photo-1421903.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1','https://images.pexels.com/photos/1612353/pexels-photo-1612353.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',]

# Create your views here.
def index(request):
    context = {
        'photos': photos
    }
    return render(request, 'gallery/home.html', context)
