from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request,"index.html")


def about_us(request):
    return render(request,"about-us.html")

def contact_us(request):
    return render(request,"contact-us.html")

def faq(request):
    return render(request,"faq.html")