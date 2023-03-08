from django.urls import path
from .import views
urlpatterns = [
    path('Admin-DashBoard',views.dashboard,name='dashboard'),
]