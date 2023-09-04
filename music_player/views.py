from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    music = Song.objects.all()
    return render(request, 'home.html', {'songs':music})