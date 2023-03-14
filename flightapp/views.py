from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def dashboard(request):
    
    return render(request,'admin/admindashboard.html')
def seatbooking(request):
    
    return render(request,'web/seatbooking.html')

def base(request):
    
    return render(request,'base.html')

def flight_signin(request):

    return render(request,'flight_signin.html')

def flight_signup(request):

    return render(request,'flight_signup.html')

def signupcreate(request):
    print("hhhhhhhh")
    if request.method=="POST":
        unam=request.POST["uname"]
        mail=request.POST["email"]
        pwd=request.POST["password"]
        if User.objects.filter(username=unam).exists():
            messages.info(request,"User does not exist")
            return redirect('flight_signup')
        else:
            user=User.objects.create_user(username=unam,password=pwd,email=mail)
            user.save()
        return redirect('flight_signin')

def addpassenger(request):
    return render(request,'web/passenger.html')


def addform(request):
    return render(request,'admin/adminform.html')    
def addform2(request):
    return render(request,'admin/adminform2.html')    
def addpayment(request):
    return render(request,'web/payment.html')        
   
