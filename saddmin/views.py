from django.shortcuts import render, redirect
from .models import ContactUs, postEquiry, propertyType, cityName,stateName,Country
from django.contrib.auth.models import User, AbstractUser
from django.contrib import messages
from datetime import datetime
from django.views.generic import ListView, DetailView

# Create your views here.
def dashboard(request):
    prop_obj = propertyType.objects.all()
    state_obj = stateName.objects.all()
    city_obj = cityName.objects.all()
    myuser = User.objects.all()
    prop_counts = prop_obj.count()
    state_count = state_obj.count()
    city_count = city_obj.count()
    user_count = myuser.count()
    total_enquiry = postEquiry.objects.all().count()
    # print(total_enquiry)
    obj=User.objects.get(is_superuser=1)
    current_user_property = propertyType.objects.filter(create_by=obj.id).count()
    # print(current_user)
    objs=User.objects.get(broker=1)
    count_agent_property = propertyType.objects.filter(create_by=objs.id).count()
    return render(request, "dashboard.html", {'prop_counts':prop_counts,'state_count':state_count,'city_count':city_count,'user_count':user_count,'total_enquiry':total_enquiry, 'current_user_property':current_user_property,'count_agent_property':count_agent_property})


# -----------------------------------START Country CRUD--------------------------------------
def country(request):
    
    if request.method == "POST":
        name = request.POST['name']
        
        obj = Country(name=name)
        obj.save()
        messages.success(request,"Country Has Been Added Successfully!")   
        print(obj.name)   #for add data into database
        
        return render(request, "add_country.html")

    else:
        return render(request, "add_country.html")


def getcountry(request):
    contry_obj = Country.objects.all()
    print(contry_obj)
    return render(request, "show_country.html", {'contry_obj': contry_obj})


def deletecountry(request, id):
    dobj = Country.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saddmin/getcountry/')
    

def updatecountry(request, id):
    if request.method == 'POST':
        name = request.POST['country']
       
        cobj = Country.objects.filter(id=id)  # QuerySet
        cobj.update(name=name)

        return redirect('/saddmin/getcountry/')

    else:
        c = Country.objects.get(id=id)
        return render(request, "country-update.html", {'data': c})

# -----------------------------------END Country CRUD--------------------------------------

# -----------------------------------START PROPERTY CRUD---------------------------------------
def properties(request):
    cobjs = propertyType.objects.all()
    data = stateName.objects.all()
    print(data)
    if request.method == "POST":
        name = request.POST['name']
        status = request.POST['status']
        state = request.POST['state_id']
        city = request.POST['city']
        room = request.POST['room']
        beds = request.POST['beds']
        baths = request.POST['baths']
        squer_fit = request.POST['squer_fit']
        overview = request.POST['overview']
        amount = request.POST['amount']
        pro_img = request.FILES['pro_img']
        create_by = request.user.id

        # print(create_by)
        
        # uobj = User.objects.get(username=request.user)
        obj = propertyType(name=name,state_id=state,city=city,pro_img=pro_img,status=status,room=room,beds=beds,baths=baths,squer_fit=squer_fit,overview=overview,amount=amount,create_by=create_by)
        obj.save()
        messages.success(request,"Property Has Been Added Successfully!")   
        # print(obj.name)   #for add data into database
        # print(obj.pro_img)
        return render(request, "property-type.html", {'cobjs':cobjs})

    else:
        return render(request, "property-type.html", {'data':data})

def getproperties(request):
    contry_objs = Country.objects.all()
    cobjs = propertyType.objects.all()
    property_count = propertyType.objects.all().count()
    
    return render(request, "properties.html", {'cobjs': cobjs,'count_obj':property_count,'contry_objs':contry_objs})

class BlogSearchView(ListView):
    model = propertyType
    template_name: 'properties.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return propertyType.objects.filter(amount__icontains=query).order_by('-created_at')

def deleteproperty(request, id):
    dobj = propertyType.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saddmin/getproperties/')
    

def updateproperty(request, id):
    if request.method == 'POST':
        name = request.POST['name']

        cobj = propertyType.objects.filter(id=id)  # QuerySet
        cobj.update(name=name)

        return redirect('/saddmin/getproperties/')

    else:
        c = propertyType.objects.get(id=id)
        return render(request, "property-type-update.html", {'data': c})
        

# -----------------------------------END PROPERTY CRUD---------------------------------------


# -----------------------------------START STATUS CRUD--------------------------------------
def state(request):
    data= Country.objects.all()
    print(data)
    if request.method == "POST":
        name = request.POST['name']
        country_id=request.POST['country_id']

        if name == "":
            return redirect('/saddmin/city/')
        
        obj = stateName(name=name,country_id=country_id)
        obj.save()
        messages.success(request,"State Has Been Added Successfully!")   
        # print(obj.name)   #for add data into database
        
        return render(request, "add_state.html")

    else:
        return render(request, "add_state.html", {'mydata': data})


def getstate(request):
    cobjs = stateName.objects.all()
    contry_obj = Country.objects.all()
    return render(request, "show_state.html", {'cobjs': cobjs,'contry_obj':contry_obj})


def deletestate(request, id):
    dobj = stateName.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saddmin/getstate/')
    

def updatestate(request, id):
    if request.method == 'POST':
        name = request.POST['name']
       
        cobj = stateName.objects.filter(id=id)  # QuerySet
        cobj.update(name=name)

        return redirect('/saddmin/getstate/')

    else:
        c = stateName.objects.get(id=id)
        return render(request, "state-update.html", {'data': c})

# -----------------------------------END STATE CRUD--------------------------------------


# -----------------------------------START CITY CRUD--------------------------------------
def city(request):
    country_data= Country.objects.all()
    state_data= stateName.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        state_id = request.POST['state_id']
        country_id = request.POST['country_id']
        
        obj = cityName(name=name,state_id=state_id,country_id=country_id)
        obj.save()
        messages.success(request,"City Has Been Added Successfully!")   
        print(obj.name)   #for add data into database
        
        return render(request, "add_city.html")

    else:
         return render(request, "add_city.html", {'mystate':state_data,'mycountry':country_data})

def getcity(request):
    cobjs = cityName.objects.all()
    return render(request, "show_city.html", {'cobjs': cobjs})

def deletecity(request, id):
    dobj = cityName.objects.get(id=id)
    dobj.delete()
    messages.success(request,"Successfully deleted")
    return redirect('/saddmin/getcity/')
    

def updatecity(request, id):
    country_data= Country.objects.all()
    state_data= stateName.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        state_id = request.POST['state_id']
        country_id = request.POST['country_id']

        cobj = cityName.objects.filter(id=id)  # QuerySet
        cobj.update(name=name,state_id=state_id,country_id=country_id)
        messages.success(request, "City Updated Successfully..")
        return redirect('/saddmin/updatecity/')

    else:
        c = cityName.objects.get(id=id)
        return render(request, "city-update.html", {'data': c,'mystate':state_data,'mycountry':country_data})
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

def Agent(request):
    obj=User.objects.get(broker=1)
    split_obj = propertyType.objects.filter(create_by= obj.id)
    print(obj.id)
    return render(request, "show_agent_property.html", {'split_obj':split_obj})

def Contact_us(request):
    client = ContactUs.objects.all()
    return render(request, "show_user_info.html", {'client':client})

def connect_to_client(request):
    my_client = postEquiry.objects.all().order_by('id').reverse()
    return render(request, "Intrasted_client.html", {'int_client':my_client})   


