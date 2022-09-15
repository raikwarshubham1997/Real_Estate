from venv import create
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from saddmin.models import propertyType, cityName,stateName,Country,postEquiry


#  user registration 
def Business_ac(request):
	if request.method == "POST":
		nm = request.POST['nm']
		lnm = request.POST['lnm']
		email = request.POST['email']
		uname = request.POST['un']
		pwd = request.POST['pwd']
		
		date = datetime.now()
		

		u = User(first_name=nm, last_name=lnm, email=email, username=uname, password=make_password(pwd), broker=True,date_joined=date)
		u.save()
		messages.success(request,"Registration Successfully Done")
		return redirect('/register/')
	return render(request, "broker_register.html")

def login_saler(request):
	if request.method == "POST":
		uname = request.POST['un']
		pwd = request.POST['pwd']

		user = authenticate(username=uname, password=pwd)
		print(user.date_joined)

		if user:
			login(request, user)
			if user.broker:
				return redirect('/saler/dashboard/')
            
		else:
			return redirect('/login/')
		
	return render(request, "login_saler.html")

def logout_call(request):
	logout(request)
	return redirect('/login/')


def broker_index(reuest):
    return render(reuest, "broker_index.html")

# Create your views here.
def dashboard(request):
    user_id = request.user.id
    print(user_id)
    prop_obj = propertyType.objects.filter(create_by=user_id).count()
    return render(request, "broker_index.html", {'prop_obj':prop_obj})



# -----------------------------------START PROPERTY CRUD---------------------------------------
def properties(request):
    cobjs = propertyType.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        status = request.POST['status']
        room = request.POST['room']
        beds = request.POST['beds']
        baths = request.POST['baths']
        squer_fit = request.POST['squer_fit']
        overview = request.POST['overview']
        amount = request.POST['amount']
        pro_img = request.FILES['pro_img']
        create_by = request.user.id
        
        # uobj = User.objects.get(username=request.user)
        obj = propertyType(name=name,pro_img=pro_img,status=status,room=room,beds=beds,baths=baths,squer_fit=squer_fit,overview=overview,amount=amount,create_by=create_by)
        obj.save()
        messages.success(request,"Property Has Been Added Successfully!")   
        # print(obj.name)   #for add data into database
        # print(obj.pro_img)
        return render(request, "property-add_by_broker.html", {'cobjs':cobjs})

    else:
        return render(request, "property-add_by_broker.html")

def getproperties(request):
    user_id =request.user.id       # current logged in User
    cobjs = propertyType.objects.filter(create_by=user_id)
    property_count = propertyType.objects.all().count()
    
    return render(request, "show_broker_properties.html", {'cobjs': cobjs, 'property_count':property_count})



def deleteproperty(request, id):
    dobj = propertyType.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saler/getproperties/')
    

def updateproperty(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        pro_img = request.FILES['pro_img']

        cobj = propertyType.objects.filter(id=id)  # QuerySet
        cobj.update(name=name,pro_img=pro_img)

        return redirect('/saler/getproperties/')

    else:
        c = propertyType.objects.get(id=id)
        return render(request, "property-type-update.html", {'data': c})
        

# -----------------------------------END PROPERTY CRUD---------------------------------------


# -----------------------------------START STATUS CRUD--------------------------------------
def state(request):
    if request.method == "POST":
        name = request.POST['name']
        # country_id = request.POST['name']

        if name == "":
            return redirect('/saler/city/')
        
        obj = stateName(name=name)
        obj.save()
        messages.success(request,"State Has Been Added Successfully!")   
        # print(obj.name)   #for add data into database
        
        return render(request, "add_state_by_broker.html")

    else:
        return render(request, "add_state_by_broker.html")


def getstate(request):
    cobjs = stateName.objects.all()
    contry_obj = Country.objects.all()
    return render(request, "show_state_by_broker.html", {'cobjs': cobjs,'contry_obj':contry_obj})


def deletestate(request, id):
    dobj = stateName.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saler/getstate/')
    

def updatestate(request, id):
    if request.method == 'POST':
        name = request.POST['name']
       
        cobj = stateName.objects.filter(id=id)  # QuerySet
        cobj.update(name=name)

        return redirect('/saler/getstate/')

    else:
        c = stateName.objects.get(id=id)
        return render(request, "state-update_by_broker.html", {'data': c})

# -----------------------------------END STATE CRUD--------------------------------------


# -----------------------------------START CITY CRUD--------------------------------------
def city(request):
    if request.method == "POST":
        name = request.POST['name']
        
        obj = cityName(name=name)
        obj.save()
        messages.success(request,"City Has Been Added Successfully!")   
        print(obj.name)   #for add data into database
        
        return render(request, "add_city_by_broker.html")

    else:
         return render(request, "add_city_by_broker.html")

def getcity(request):
    cobjs = cityName.objects.all()
    return render(request, "show_city_by_broker.html", {'cobjs': cobjs})

def deletecity(request, id):
    dobj = cityName.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saler/getcity/')
    

def updatecity(request, id):
    if request.method == 'POST':
        name = request.POST['name']
       
        cobj = cityName.objects.filter(id=id)  # QuerySet
        cobj.update(name=name)

        return redirect('/saler/getcity/')

    else:
        c = cityName.objects.get(id=id)
        return render(request, "city-update_by_broker.html", {'data': c})
# -----------------------------------END CITY CRUD--------------------------------------

# from django.shortcuts import render
# # Create your views here.
# def index(request):
#     probj = propertyType.objects.all()
#     stateobj = stateName.objects.all()
#     cobjs = cityName.objects.all()
#     return render(request, "index.html", {'probj':probj,'stateobj':stateobj, 'cobjs':cobjs})

def user(request):
    myuser = User.objects.all()
    print(myuser)
    return render(request, "users.html", {'myuser': myuser})


def logouts(request):
    logout(request)
    return redirect('/saler/logout/')


def client_Enquiry(request):
    objs=User.objects.get(broker=1)
    count_agent_property = postEquiry.objects.filter(create_by=objs.id)
    print(count_agent_property)

    
    return render(request, "client_Enquiry.html",{'count_agent_property':count_agent_property})