from django.shortcuts import render

# Create your views here.
def dashboard(request):
    
    return render(request,'admin/admindashboard.html')
def seatbooking(request):
    
    return render(request,'web/seatbooking.html')

   
