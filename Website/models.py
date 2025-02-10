from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class TalentCategories(models.Model):
    category_title=models.CharField(max_length=200,unique=True)
    category_img=models.FileField(upload_to=f"images/categories",default="images/categories/category-default.jpg")


    def __str__(self):
	    return self.category_title
    

class Talent(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    display_pic=models.FileField(upload_to=f"images/talents",default="images/talents/default-DP.jpg",null=False)
    first_name=models.CharField(max_length=150,null=False)
    last_name=models.CharField(max_length=150,null=False)
    other_names=models.CharField(max_length=300,null=True, blank=True)
    profession=models.CharField(max_length=300,null=False)
    gender=models.CharField(max_length=10,choices=(
        ('MALE', u'MALE'),
        ('FEMALE', u'FEMALE'),
    ),null=False)
    stage_name=models.CharField(max_length=200,null=True, blank=True)
    mantra=models.CharField(max_length=300,null=True, blank=True)
    about=models.TextField()
    image1=models.FileField(upload_to=f"images/talents",default="images/talents/talent-default.jpg",null=False)
    image2=models.FileField(upload_to=f"images/talents",null=True, blank=True)
    image3=models.FileField(upload_to=f"images/talents",null=True, blank=True)
    category = models.ForeignKey(TalentCategories, on_delete=models.CASCADE,)


    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
	    return f"{self.first_name} {self.last_name}"
    

class Advertisement(models.Model):
    advert_title= models.CharField(max_length=200,default="No Title")
    image=models.FileField(upload_to=f"images/advert",default="images/advert/advert-default.jpg",null=False)

    def __str__(self):
	    return self.advert_title