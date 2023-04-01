from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from flightapp.models import airportcode, city, experiences, flight, trip, hotel, testimonial


# Create your views here.


@login_required(login_url='flight_signin') 
def seatbooking(request):
    return render(request,'web/seatbooking.html')

def base(request):
    hotel1=hotel.objects.all().order_by('-id')[:3]
    city1=city.objects.all().order_by('-id')[:3]
    test=testimonial.objects.all().order_by('-id')[:3]
    return render(request,'base.html',{'hotel':hotel1,'city':city1,'test':test})

def home(request):
    city_view=city.objects.all()
    details=flight.objects.all()
    return render(request,'home.html',{'city_view':city_view})

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


def admincity(request):
    city1=city.objects.all()
    return render(request,'admin/addcity.html',{'city':city1})

def admin_city_add(request):
    if request.method=='POST':
        name=request.POST['name']
        city_name=request.POST['city']
        description=request.POST['des']
        price=request.POST['price']
        image=request.FILES['file']
        city_details=city(name=name,city=city_name,description=description,price=price,image=image)
        city_details.save()
        messages.success(request, 'City details added sucessfully!')
    return redirect('admincity')


def deletecity(request,id):
    member1 = city.objects.get(id=id)
    member1.delete()
    messages.error(request, 'city details deleted sucessfully!')
    return redirect('admincity')  


def admintestimonial(request):
    test=testimonial.objects.all()
    return render(request,'admin/testimonial.html',{'test':test})

def addtestimonial(request):
    if request.method=='POST':
        name=request.POST['name']
        date1=request.POST['date']
        date2=datetime.strptime(date1,'%Y-%m').date()
        city=request.POST['city']
        country=request.POST.get('country')
        message=request.POST['des']
        rate=request.POST.get('rate')
        image=request.FILES['file']
        testi=testimonial(name=name,date=date2,city=city,country=country,rating=rate,message=message,image=image)
        testi.save()
        messages.success(request, 'testimonial added sucessfully!')
        return redirect('admintestimonial')

def deletetestimonial(request,id):
    member1 = testimonial.objects.get(id=id)
    member1.delete()
    messages.error(request, 'testimonial details deleted sucessfully!')
    return redirect('admintestimonial') 


def airport(request):
    test=airportcode.objects.all()
    return render(request,'admin/airport.html',{'airport':test})


def saveairport(request):
    if request.method=='POST':
        city=request.POST['city']
        country=request.POST['con']
        code=request.POST['code']
        code1=airportcode(city=city,country=country,code=code)
        code1.save()
        messages.success(request, 'details added sucessfully!')
        return redirect('airport') 
    else:
        return redirect('airport') 



def deleteairport(request,id):
    member1 =airportcode.objects.get(id=id)
    member1.delete()
    messages.error(request, 'details deleted sucessfully!')
    return redirect('airport') 


def adminflight(request):
    test=flight.objects.all()
    return render(request,'admin/adminflight.html',{'flight1':test})

def saveflight(request):
    if request.method=='POST':
        name=request.POST['name']
        code=request.POST['code']
        image=request.FILES['file']
        code1=flight(flightname=name,code=code,logo=image)
        code1.save()
        messages.success(request,'Flight details added sucessfully!')
        return redirect('adminflight') 
    else:
        return redirect('adminflight') 
    
def deleteflight(request,id):
    member1 =flight.objects.get(id=id)
    member1.delete()
    messages.error(request, 'details deleted sucessfully!')
    return redirect('adminflight') 
    
def admintrip(request):
    flight1=flight.objects.all().order_by('flightname')
    code1=airportcode.objects.all().order_by('code')
    return render(request,'admin/admintrip.html',{'flight':flight1,'code':code1})    






