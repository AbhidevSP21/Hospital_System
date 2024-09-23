from django.urls import path,include
from .import views

urlpatterns = [
    path('login',views.login_access,name='login'),
    path('',views.index,name='index'),
    path('doctorlist',views.doctorlist,name='doctorlist'),
    path('feedback',views.feedback,name='feedback'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('patient_register',views.patient_register,name='patient_register'),
    path('user_login',views.user_login,name='user_login'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('logout',views.user_logout,name='logout'),
    path('appointment',views.appointment,name="appointment"),
    path('prediction',views.prediction,name="prediction"),


]