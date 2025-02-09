from django.shortcuts import render

# Create your views here.

from .models import Tour

def home_view(request):
    tours = Tour.objects.all()
    context = {
        'tours':tours
    }
    return render(request, "index.html", context)
