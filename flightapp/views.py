from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from flightapp.models import experiences, hotel


# Create your views here.


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
            if user.is_staff:
                auth.login(request,user)
                request.session["uid"]=user.id
                return redirect('dashboard')
            
            else:
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

@login_required(login_url='flight_signin') 
def afterpayment(request):
    hotel1=hotel.objects.all().order_by('-id')[:4]
    exp1=experiences.objects.all().order_by('-id')[:2]
    return render(request,'web/afterpayment.html',{'hotel':hotel1,'exp':exp1})
#------------------------admin section---------------------------


@login_required(login_url='/flight_signin') 
def dashboard(request):
    return render(request,'admin/adminbase.html')



def resetpassword(request):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
    data=User.objects.get(id=uid)
    return render(request,'admin/adminpassword.html',{'data':data})
   
def resetpass(request,user_id):
    if 'uid' in request.session:
        if request.session.has_key('uid'):
            uid = request.session['uid']
        else:
            return redirect('/')
        user = User.objects.get(pk=user_id)
        user.username= request.POST.get('name')
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        data=User.objects.get(id=uid)
        messages.success(request, 'Password updated sucessfully!')
        return render(request,'admin/adminpassword.html',{'data':data})
    else:
        return redirect('flight_signin')
    
@login_required(login_url='/flight_signin') 
def addhotel(request):
    hotel1=hotel.objects.all()
    return render(request,'admin/addhotel.html',{'hotel':hotel1})


def savehotel(request):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        city=request.POST['city']  
        des=request.POST['des']   
        image=request.FILES['file']
        data = hotel(name=name,city=city,price=price,description=des,image=image)
        data.save()
        messages.success(request, 'hotel details added sucessfully!')
    return redirect('addhotel')


def deletehotel(request,id):
    member = hotel.objects.get(id=id)
    member.delete()
    messages.error(request, 'one hotel details deleted sucessfully!')
    return redirect('addhotel')

@login_required(login_url='/flight_signin') 
def addexp(request):
    exp1=experiences.objects.all()
    return render(request,'admin/addexperience.html',{'exp':exp1})

def saveexp(request):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        city=request.POST['city']  
        des=request.POST['des']   
        image=request.FILES['file']
        data = experiences(name=name,city=city,price=price,description=des,image=image)
        data.save()
        messages.success(request, 'experience details added sucessfully!')
    return redirect('addexp')

def deleteexp(request,id):
    member1 = experiences.objects.get(id=id)
    member1.delete()
    messages.error(request, 'one experience details deleted sucessfully!')
    return redirect('addexp')    

def adminbooking(request):
    exp1=experiences.objects.all()
    return render(request,'admin/booking.html')

@login_required(login_url='/flight_signin') 
def logout(request):
    auth.logout(request)
    return redirect('base')

