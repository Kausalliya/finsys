from django.urls import path
from .import views
urlpatterns = [
    path('',views.base,name='base'),
    path('flight_signin',views.flight_signin,name='flight_signin'),
    path('flight_signup',views.flight_signup,name='flight_signup'),
    path('signupcreate',views.signupcreate,name='signupcreate'),
    path('Admin-DashBoard',views.dashboard,name='dashboard'),
    path('seatbooking',views.seatbooking,name='seatbooking'),
    path('addpassenger',views.addpassenger,name='addpassenger'),
    path('addform',views.addform,name='addform'),
    path('addform2',views.addform2,name='addform2'),
    path('addpayment',views.addpayment,name='addpayment'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('afterpayment',views.afterpayment,name='afterpayment'),






]