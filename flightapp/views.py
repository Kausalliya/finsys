from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def dashboard(request):
    
    return render(request,'admin/admindashboard.html')

@login_required(login_url='flight_signin') 
def seatbooking(request):
    return render(request,'web/seatbooking.html')

def base(request):
    
    return render(request,'base.html')

def flight_signin(request):
    return render(request,'flight_signin.html')

def signin(request):
    print("hai")
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base')
            
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('flight_signin') 
        
def flight_signup(request):
    return render(request,'flight_signup.html')

def signupcreate(request):
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

@login_required(login_url='/flight_signin')      
def addpassenger(request):
    return render(request,'web/passenger.html')


def addform(request):
    return render(request,'admin/adminform.html')    
def addform2(request):
    return render(request,'admin/adminform2.html')  

@login_required(login_url='flight_signin')    
def addpayment(request):
    return render(request,'web/payment.html')        
   
def logout(request):
    auth.logout(request)
    return redirect('flight_signin')

def afterpayment(request):
    return render(request,'web/afterpayment.html')