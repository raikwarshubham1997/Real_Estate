from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from saddmin.models import propertyType, cityName,stateName,ContactUs,postEquiry
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    probj = propertyType.objects.all()
    stateobj = stateName.objects.all()
    cobjs = cityName.objects.all()

    # # pagination apply property
    # paginator = Paginator(probj, 3)
    # page_number = request.GET.get('page')
    # property_datafinal = paginator.get_page(page_number)
    
    
    return render(request, "index.html", {'probj':probj,'stateobj':stateobj, 'cobjs':cobjs})

def about(request):
    return render(request, "about.html")

def propertydetail(request, id):
    obj = propertyType.objects.get(id=id)
    return render(request, "properties-detail.html", {'obj' : obj})

def contact(request):
    if request.method == 'POST':
        author = request.POST['author'] 
        email = request.POST['email'] 
        subject = request.POST['subject'] 
        comment = request.POST['comment']
        

        obj = ContactUs(author=author, email=email, subject=subject, comment=comment)
        obj.save()
        messages.success(request, "Your Details successfully Submited")
    return render(request, "contact.html")


def post_enqiry(request,id):
    data= propertyType.objects.get(id=id)   # get forign key by property type table
    print(data)
    if request.method == 'POST':
        fullname = request.POST['fullname'] 
        email = request.POST['email'] 
        contact = request.POST['contact'] 
        comment = request.POST['comment']
        date = datetime.now()
        postEquiry.objects.create(property_Id=data,fullname=fullname, email=email, contact=contact, comment=comment, date=date)
        messages.success(request, "We Will Contact With You Soon....")
        return redirect('/user/index/')
    else:
        return render(request, "contact.html")

