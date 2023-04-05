from datetime import datetime
import time
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
import pandas as pd

from flightapp.models import airportcode, city, experiences, flight, stops, trip, hotel, testimonial


# Create your views here.


@login_required(login_url='flight_signin') 
def seatbooking(request):
    return render(request,'web/seatbooking.html')

def base(request):
    hotel1=hotel.objects.all().order_by('-id')[:3]
    city1=city.objects.all().order_by('-id')[:3]
    test=testimonial.objects.all().order_by('-id')
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
    trip1=trip.objects.all().order_by('id')
    return render(request,'admin/admintrip.html',{'flight':flight1,'code':code1,'trip':trip1})    


def addtrip(request):
    if request.method=='POST':
        from_w=request.POST['from']
        to_w=request.POST['toplace']
        ddate=request.POST['ddate']
        ddate1 = datetime.strptime(ddate,'%Y-%m-%dT%H:%M')
        ddate2=str(ddate1.year)+"-"+str(ddate1.month)+"-"+str(ddate1.day)
        dtime=str(ddate1.hour)+":"+str(ddate1.minute)
        dtime1= datetime.strptime(dtime, "%H:%M")
        dtime2=dtime1.strftime("%I:%M %p")
        adate=request.POST['adate']
        adate1 = datetime.strptime(adate,'%Y-%m-%dT%H:%M')
        adate2=str(adate1.year)+"-"+str(adate1.month)+"-"+str(adate1.day)
        atime=str(adate1.hour)+":"+str(adate1.minute)
        atime1= datetime.strptime(atime, "%H:%M")
        atime2=atime1.strftime("%I:%M %p")
        duration = adate1-ddate1
        duration_in_s = duration.total_seconds()  
        days    = divmod(duration_in_s, 86400) 
        hours   = divmod(days[1], 3600) 
        minutes = divmod(hours[1], 60)
        if days[0]==0 :
            if minutes[0]==0:
                    min=0
            else:
                min=str(minutes[0]).rstrip('.0')   
            if hours[0]==0:
                hours=0
            else:
                hours=str(hours[0]).rstrip('.0')   
            duration=str(hours)+"h "+str(min)+"m"
            
        else:
            if minutes[0]==0:
                min=0
            else:
                min=str(minutes[0]).rstrip('.0')   
            if hours[0]==0:
                hours=0
            else:
                hours=str(hours[0]).rstrip('.0')          
            duration=str(days[0]).rstrip('.0')+"days "+str(hours)+"h "+str(min)+"m" 
        print(duration)  
        stops=request.POST['stops']
        price=request.POST['price']
        flight1=request.POST['flight']
        flight2=flight.objects.get(id=flight1)
        data=trip(from_where=from_w,where_to=to_w,depart_date=ddate2,arrival_date=adate2,duration=duration,depart_time=dtime2,arrive_time=atime2,no_stops=stops,price=price,flight=flight2)
        data.save()
        messages.success(request,'Flight details added sucessfully!')
        return redirect('admintrip') 
    else:
        return redirect('admintrip') 
    
def edittrip(request,id):
    trip1=trip.objects.get(id=id)
    flight1=flight.objects.all().order_by('flightname')
    ddate1 = trip1.depart_date.strftime("%d-%m-%Y")
    adate1 = trip1.arrival_date.strftime("%d-%m-%Y")
    code1=airportcode.objects.all().order_by('code')
    atime1= datetime.strptime(trip1.arrive_time, '%I:%M %p')
    atime=atime1.strftime('%H:%M')
    dtime1= datetime.strptime(trip1.depart_time, '%I:%M %p')
    dtime=dtime1.strftime('%H:%M')
    return render(request,'admin/edittrip.html',{'flight':flight1,'code':code1,'trip':trip1,'ddate1':ddate1,'adate1':adate1,'atime':atime,'dtime':dtime}) 

def updatetrip(request,id):
    data = trip.objects.get(id=id)
    if request.method=='POST':
        data.from_where=request.POST['from']
        data.where_to= request.POST['to_place']
        print(request.POST['ddate'])
        data.depart_date=request.POST['from']
        ddate=request.POST['ddate']
        try:
            ddate1= datetime.strptime(ddate,'%Y-%m-%dT%H:%M')
        except:
            ddate1= datetime.strptime(ddate,"%d-%m-%Y %H:%M")
        ddate2=str(ddate1.year)+"-"+str(ddate1.month)+"-"+str(ddate1.day)
        dtime=str(ddate1.hour)+":"+str(ddate1.minute)
        dtime1= datetime.strptime(dtime, "%H:%M")
        dtime2=dtime1.strftime("%I:%M %p")
        adate=request.POST['adate']
        try:
            adate1 = datetime.strptime(adate,'%Y-%m-%dT%H:%M')
        except:
            adate1 = datetime.strptime(adate,'%d-%m-%Y %H:%M')
        adate2=str(adate1.year)+"-"+str(adate1.month)+"-"+str(adate1.day)
        atime=str(adate1.hour)+":"+str(adate1.minute)
        atime1= datetime.strptime(atime, "%H:%M")
        atime2=atime1.strftime("%I:%M %p")
        duration = adate1-ddate1
        duration_in_s = duration.total_seconds()  
        days    = divmod(duration_in_s, 86400) 
        hours   = divmod(days[1], 3600) 
        minutes = divmod(hours[1], 60)
        if days[0]==0 :
            if minutes[0]==0:
                    min=0
            else:
                min=str(minutes[0]).rstrip('.0')   
            if hours[0]==0:
                hours=0
            else:
                hours=str(hours[0]).rstrip('.0')   
            duration=str(hours)+"h "+str(min)+"m"
            
        else:
            if minutes[0]==0:
                min=0
            else:
                min=str(minutes[0]).rstrip('.0')   
            if hours[0]==0:
                hours=0
            else:
                hours=str(hours[0]).rstrip('.0')          
            duration=str(days[0]).rstrip('.0')+"days "+str(hours)+"h "+str(min)+"m" 

        data.depart_date=ddate2
        data.depart_time=dtime2
        data.arrival_date=adate2
        data.arrive_time=atime2
        data.duration=duration
        data.no_stops=request.POST['stops']
        data.price=request.POST['price']
        flight1=request.POST['flight']
        flight2=flight.objects.get(id=flight1)
        data.flight=flight2
        data.save()
        messages.success(request,'Flight details updated sucessfully!')
        return redirect('admintrip') 
    
def deletetrip(request,id):
    member1 =trip.objects.get(id=id)
    member1.delete()
    messages.error(request, 'Trip details deleted sucessfully!')
    return redirect('admintrip')    

def addstops(request,id):
    data =trip.objects.get(id=id)
    code1=airportcode.objects.all().order_by('code')
    stops1=stops.objects.all().filter(trip=id)
    return render(request,'admin/addstops.html',{'data':data,'code':code1,'stop':stops1})   

def savestops(request,id):
    trip1=trip.objects.get(id=id)
    if request.method=='POST':
        duration=request.POST['dura']
        place= request.POST['place']
        data=stops(duration=duration,airport_code=place,trip=trip1)
        data.save()
    messages.error(request, 'Stop details added sucessfully!')
    return redirect('addstops',id=trip1.id) 


def deletestops(request,id):
    member1 =stops.objects.get(id=id)
    print(member1.trip_id)
    member1.delete()
    messages.error(request, 'Stop details deleted sucessfully!')
    return redirect('addstops',id=member1.trip_id)  

def searchcontent(request):
    return render(request,'web/searchcontent.html')    








