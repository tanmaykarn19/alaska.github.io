from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact 
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1" : "tanmay is great", 
        "variable2" : "but tanmay is a noob"
    }
    # return HttpResponse("this is my home page")
    # messages.success(request, "this is a test message")
    return render (request, "index.html", context)

def about(request):
    return render (request, "about.html")

def scale(request):
    return render(request, "scale.html")

def calibrate(request):
    return render(request, "calibrate.html")

def contact(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
    #     contact.save()
        
    return render(request, "contact.html")

def saveform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, "contact.html")