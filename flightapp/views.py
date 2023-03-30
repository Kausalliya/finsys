from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from flightapp.models import city, experiences, flight, flightdetails, hotel


# Create your views here.


@login_required(login_url='flight_signin') 
def seatbooking(request):
    return render(request,'web/seatbooking.html')

def base(request):
    return render(request,'base.html')

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


def admin_city(request):
    
    return render(request,'admin/admin_city.html')

def admin_city_add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        city_name=request.POST.get('city_name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES.get('image')
        city_details=city(name=name,city=city_name,description=description,price=price,image=image)
        city_details.save()
    return render(request,'admin/admin_city.html')

def admin_flightdetails(request):

    return render(request,'admin/admin_flightdetails.html')

def admin_flight_add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        logo=request.FILES.get('logo')
        flight_details=flightdetails(name=name,logo=logo)
        flight_details.save()
        plane=flightdetails.objects.get(id=flight_details.id)
        depart_time=request.POST.get('dptime')
        reach_time=request.POST.get('rtime')
        from_place=request.POST.get('frmplace')
        from_code=request.POST.get('frm_code')
        to_place=request.POST.get('toplace')
        to_code=request.POST.get('to_code')
        time_taken=request.POST.get('timetaken')
        ticket_rate=request.POST.get('rate')
        no_of_stops=request.POST.get('stop')
        depart_day=request.POST.get('day')
        flight_timing=flight(depart_time=depart_time,reach_time=reach_time,from_place=from_place,to_place=to_place,plane=plane,time_taken=time_taken,ticket_rate=ticket_rate,depart_day=depart_day,no_of_stops=no_of_stops,from_code=from_code,to_code=to_code)
        flight_timing.save()     

    return render(request,'admin/admin_flightdetails.html')


