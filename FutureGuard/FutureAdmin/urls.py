from django.urls import path,include
from .import views

urlpatterns = [
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('adminappointments',views.adminappointments,name='adminappointments'),
    path('admindoctors',views.admindoctors,name='admindoctors'),
    path('adminpatients',views.adminpatients,name='adminpatients'),
    path('adminsettings',views.adminsettings,name='adminsettings'),

]