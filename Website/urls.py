from django.urls import path
from . import views


urlpatterns =[
path("", views.home, name='home-page'),
path("about-us/", views.about_us, name='about-page'),
path("contact-us/", views.contact_us, name='contact-page'),
path("FAQs/", views.faq, name='faqs-page'),
path("talents/categories/", views.talent_category, name='talent-categories'),
path("talents/category/<str:category>/", views.talents, name='talents-page'),
path("talent/profile/<str:talent_id>/", views.talent_profile, name='talent-profile'),

]
