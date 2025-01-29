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

def talent_category(request):
    return render(request,"talent/talent-categories.html")

def talents(request,category):
    print(category)
    return render(request,"talent/talents.html",{"category":category})

def talent_profile(request,talent_name):
    return render(request,"talent/talent-profile.html", {"name":talent_name})