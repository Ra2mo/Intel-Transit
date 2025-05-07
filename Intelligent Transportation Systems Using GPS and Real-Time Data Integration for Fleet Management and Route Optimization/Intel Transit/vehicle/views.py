from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import make_password
from .models import *
import time
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
#the first was the first namin g of this function and now its 

def sign(request):
     if request.method=="POST":
        if request.POST:
            first_name=request.POST["firstname"]
            second_name=request.POST["secondname"]
            pass_word=make_password(request.POST["password"])
            company_name=request.POST["company_name"]
            usernames=request.POST["username"]
            emails=request.POST["username"]
            admins.objects.create(firstname=first_name,email=emails,secondname=second_name,password=pass_word, username=usernames,companyname=company_name)
            return render(request,"signup.html")
     return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        if request.POST:
           usernames=request.POST["username"]
           pass_word=request.POST["fisrtname"]
           if admins.objects.filter(username=usernames,secondname=pass_word).all().values() is not None:
            return render(request,"dashboard.html")
           else:
              return render(request,"home.html")  
    else:
        return render(request,"home.html")
#@login_required(login_url="logins")    
def setups(request):
    if request.method=="POST":
        if request.POST:
            vehicle_id=request.POST["vehicleid"]
            makes=request.POST["make"]
            car_models=request.POST["model"]
            vins=request.POST["vin"]
            vihecle_license=request.POST["license"]
            vehicleregistations.objects.create(vehicle_iD=vehicle_id,make=makes,car_model=car_models,license=vihecle_license, Vin=vins)
            render(request,"setup.html")
    return render(request,"setup.html") 
#@login_required(login_url="logins")   
def dasboard(request):
    return render(request,"dashboard.html") 
#@login_required(login_url="logins")
def fleetmngt(request):
    if request.method=="POST":
        if request.POST:
            hist=request.POST["vehicle_id"]
            ry=routemangt.objects.filter(vehicle_id=hist).all().values()
            context={"history":ry}
            return render(request,"homepage.html",context)
    return render(request,"fleetmnt.html") 
#@login_required(login_url="logins")
def route(request):
    return render(request,"routemngt.html")
#@login_required(login_url="logins")
def freettracking(request):
    return render(request,"fl.html")
#@login_required(login_url="logins")
def drivermngt(request):
     if request.method=="POST":
        if request.POST: 
         name=request.POST["driverid"]
        ryt=driversreg.objects.filter(Driver_id=name).all().values()
        context={"driverprofile":ryt}
        return render(request,"driverprofilev.html",context)
     else:     
      return render(request,"drivermanagement.html")
#@login_required(login_url="logins")  
def report(request):
    if request.method=="POST":
        if request.POST:
            hist2=request.POST["obara"]
            ryt=vehiclemaintance.objects.filter(vehicle_id=hist2).all().values()
            context={"maintance":ryt}
            return render(request,"moremaintance.html",context)
            
    return render(request,"report.html")
#@login_required(login_url="logins")
def notification(request):
    return render(request,"notification.html")
#@login_required(login_url="logins")
def drivereg(request):
    if request.method=="POST":
        if request.POST: 
         name=request.POST["name"]
         driver_id=request.POST["driverid"]
         licesence_type=request.POST["license_type"]
         contact_info=request.POST["contactInfo"]
         driversreg.objects.create(firstname=name,Driver_id=driver_id,license_Type=licesence_type,Phonenumber=contact_info)
         return render(request,"driverinfo.html")
    return render(request,"driverinfo.html")#this is driver form information
#@login_required(login_url="logins")
def carreg(request):
    if request.method=="POST":
        if request.POST:
            vehicle_ids=request.POST["vehicleid"]
            route_start=request.POST["startlocation"]
            endlocation=request.POST["endlocation"]
            distances=request.POST["distanceinkilometer"]
            times=time.ctime()
            routemangt.objects.create(vehicle_id=vehicle_ids,start_location=route_start,end_location=endlocation,distance=distances,date=times)
            return render(request,"rootmngt.html")
    return render(request,"rootmngt.html")#this is for root management only words i miss used

def driverupdate(request):
     if request.method=="POST":
        if request.POST:
            first_name=request.POST["vehicleid"]
            second_name=request.POST["lastservicedate"]
            pass_word=request.POST["maintancetype"]
            usernames=request.POST["nextscheduled"]
            #tim=time.ctime()
            vehiclemaintance.objects.create(vehicle_id=first_name,last_service=second_name,maintanance_type=pass_word,next_scheduled_service=usernames)
            return render(request,"randomuser.html")
     else:      
         return render(request,"randomuser.html")  
     