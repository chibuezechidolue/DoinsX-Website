from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class TalentCategories(models.Model):
    category_title=models.CharField(max_length=200,unique=True)
    category_img=models.FileField(upload_to=f"media/categories",default="category-default.jpg")


    def __str__(self):
	    return self.category_title
    

class Talent(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    first_name=models.CharField(max_length=150,null=False)
    last_name=models.CharField(max_length=150,null=False)
    other_names=models.CharField(max_length=300,null=True, blank=True)
    profession=models.CharField(max_length=300,null=False)
    product_gender=models.CharField(max_length=10,choices=(
        ('MALE', u'MALE'),
        ('FEMALE', u'FEMALE'),
    ),null=False)
    stage_name=models.CharField(max_length=200,null=True, blank=True)
    height=models.CharField(max_length=20,null=True, blank=True)
    about=models.TextField()
    image1=models.FileField(upload_to=f"media/talents",default="talent-default.jpg",null=False)
    image2=models.FileField(upload_to=f"media/talents",null=True, blank=True)
    image3=models.FileField(upload_to=f"media/talents",null=True, blank=True)
    category = models.ForeignKey(TalentCategories, on_delete=models.CASCADE,)


    def __str__(self):
	    return f"{self.first_name} {self.last_name}"
    

class Advertisement(models.Model):
    image1=models.FileField(upload_to=f"media/advert",default="advert-default.jpg",null=False)
    image2=models.FileField(upload_to=f"media/advert",null=True, blank=True)
    image3=models.FileField(upload_to=f"media/advert",null=True, blank=True)
    image4=models.FileField(upload_to=f"media/advert",null=True, blank=True)
    image5=models.FileField(upload_to=f"media/advert",null=True, blank=True)

    def __str__(self):
	    return "Advertisement"