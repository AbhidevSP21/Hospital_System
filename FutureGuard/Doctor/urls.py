from django.urls import path
from . import views

urlpatterns = [
    path('doctor_profile', views.doctor_profile, name='doctor_profile'),
]
