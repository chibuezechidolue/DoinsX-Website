from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator
from dotenv import load_dotenv
from .models import (TalentCategories,Talent,Advertisement) 
import random
import os

load_dotenv()
# Create your views here.


def home(request):
    adverts=Advertisement.objects.all()
    talents=list(Talent.objects.all())
    random.shuffle(talents)
    return render(request,"index.html",{"adverts":adverts,"talents":talents[:4]})


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
                from_email=os.environ.get('EMAIL_USERNAME'),
                recipient_list=[os.environ.get('RECIPIENT_EMAIL'),],  
            )
        messages.add_message(request, messages.SUCCESS, "Your message was sent successfully")
        return redirect('home-page')
    return render(request,"contact-us.html")

def faq(request):
    return render(request,"faq.html")

def talent_category(request):
    talent_category=TalentCategories.objects.all().order_by("id")

    paginator = Paginator(talent_category, 5)  # Show 5 products per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"talent/talent-categories.html",{"page_obj":page_obj,})

def talents(request,category):
    current_category=TalentCategories.objects.get(category_title=category.title())
    talents= Talent.objects.filter(category_id=current_category.id).order_by("id")

    paginator = Paginator(talents, 6)  # Show 6 products per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj[0].first_name)
    return render(request,"talent/talents.html",{"page_obj":page_obj,"category_img":current_category.category_img})

def talent_profile(request,talent_id):
    talent= Talent.objects.get(id=talent_id)
    return render(request,"talent/talent-profile.html", {"talent":talent})