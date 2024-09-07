from django.urls import path,include
from .import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.index,name='index'),
    path('doctorlist',views.doctorlist,name='doctorlist'),
    path('feedback',views.feedback,name='feedback'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),

]