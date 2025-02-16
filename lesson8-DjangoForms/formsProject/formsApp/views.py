from django.shortcuts import render, redirect
from .forms import ContactForm


def home_view(request):
        return render(request,'pages/home.html')

def contact_view(request):
        
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                return redirect('contact_success')
        form = ContactForm()
        return render(request,'pages/contact.html', {'form':form})

def contact_success_view(request):
        return render(request,'pages/contact_success.html')