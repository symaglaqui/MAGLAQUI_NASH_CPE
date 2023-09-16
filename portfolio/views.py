from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'home.html')
def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()

        messages.success(request, "Thank you!Your message has been sent!")
        return render(request, 'home.html')
    return render(request, 'contact.html')