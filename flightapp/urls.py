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

    path('admincity',views.admincity,name='admincity'),
    path('admin_city_add',views.admin_city_add,name='admin_city_add'),
    path('admin_flightdetails',views.admin_flightdetails,name='admin_flightdetails'),
    path('admin_flight_add',views.admin_flight_add,name='admin_flight_add'),
    path('deletecity/<int:id>', views.deletecity, name='deletecity'),

    path('admintestimonial',views.admintestimonial,name='admintestimonial'),
    path('addtestimonial',views.addtestimonial,name='addtestimonial'),
    path('deletetestimonial/<int:id>', views.deletetestimonial, name='deletetestimonial'),










]