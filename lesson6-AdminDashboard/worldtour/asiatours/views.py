from django.shortcuts import render
from .models import Tour
# Create your views here.

def home_view(request):
    tours = Tour.objects.all()
    context = {
        'tours':tours
    }
    return render(request,'home.html', context)