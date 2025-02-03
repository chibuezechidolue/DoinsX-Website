from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.


def home(request):
    return render(request,"index.html")


def about_us(request):
    return render(request,"about-us.html")

def contact_us(request):
    if request.method=="POST":
        content = request.POST
        name=content.get('name')
        email=content['email']
        phone=content.get('phone')
        message=content.get('message')
        send_mail(
                subject='Message from DoinsXtmc Website',
                message=f"Name: {name}\nEmail: {email}\nPhone no: {phone}\nMessage: {message}",   
                from_email=None,
                recipient_list=[os.environ.get('EMAIL_USERNAME'),],  
            )
        messages.add_message(request, messages.SUCCESS, "Your message was sent successfully")
        return redirect('home-page')
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