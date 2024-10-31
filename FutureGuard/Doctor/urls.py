from django.urls import path
from . import views

urlpatterns = [
    path('doctor_profile', views.doctor_profile, name='doctor_profile'),
    path('viewappoint', views.viewappoint, name='viewappoint'),
    path('user_logout',views.user_logout,name='user_logout')
]
