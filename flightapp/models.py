from distutils.command.upload import upload
from email.policy import default
# import email
from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=30)  
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
   
         
class city(models.Model):
    name=models.CharField(max_length=30)  
    city=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image=models.ImageField( upload_to="images/",null=True,blank=True)

class flightdetails(models.Model):
    name=models.CharField(max_length=30)  
    time_taken=models.CharField(max_length=30)
    ticket_rate=models.CharField(max_length=100)
    no_of_stops=models.CharField(max_length=30)
    logo=models.ImageField( upload_to="images/",null=True,blank=True)
class flight(models.Model):
    from_place=models.CharField(max_length=30)
    from_code=models.CharField(max_length=30,null=True)
    to_place=models.CharField(max_length=30)
    to_code=models.CharField(max_length=30,null=True)
    depart_time=models.CharField(max_length=30)
    reach_time=models.CharField(max_length=30)
    plane=models.ForeignKey(flightdetails,on_delete=models.CASCADE)
