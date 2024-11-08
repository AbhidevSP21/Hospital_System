from django.urls import path,include
from .import views 

urlpatterns = [
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('adminappointments',views.adminappointments,name='adminappointments'),
    path('admindoctors',views.admindoctors,name='admindoctors'),
    path('adminpatients',views.adminpatients,name='adminpatients'),
    path('adminsettings',views.adminsettings,name='adminsettings'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('edit_doctor/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    
]