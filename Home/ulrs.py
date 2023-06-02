from django.contrib import admin
from django.urls import path 
from Home import views 

urlpatterns = [
    path("", views.index, name='Home'),
    path("about/", views.about, name='About'),
    path("checkScale/", views.scale, name='Check Scale'), 
    path("calibrate/", views.calibrate, name='Calibrate'),
    path("contact/", views.contact, name='Contact'), 
    path("saveform/", views.saveform, name='saveform')
    

]