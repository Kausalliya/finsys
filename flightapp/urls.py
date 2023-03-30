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
    path('addhotel',views.addhotel,name='addhotel'),
    path('savehotel',views.savehotel,name='savehotel'),
    path('deletehotel/<int:id>', views.deletehotel, name='deletehotel'),
    path('addexperience',views.addexp,name='addexp'),
    path('saveexp',views.saveexp,name='saveexp'),
    path('deleteexp/<int:id>', views.deleteexp, name='deleteexp'),
    path('resetpass/<int:user_id>', views.resetpass, name='resetpass'),

    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('adminbooking', views.adminbooking, name='adminbooking'),
    path('logout', views.logout, name='logout'),

    path('admin_city',views.admin_city,name='admin_city'),
    path('admin_city_add',views.admin_city_add,name='admin_city_add'),
    path('admin_flightdetails',views.admin_flightdetails,name='admin_flightdetails'),
    path('admin_flight_add',views.admin_flight_add,name='admin_flight_add'),





]