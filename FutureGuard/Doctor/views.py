from django.shortcuts import render
from Patient.models import Appointment
from FutureAdmin.models import Doctor
from django.contrib.auth import  logout 

# Create your views here.
def doctor_profile(request):
    data = Doctor.objects.filter(user_id = request.user)
    return render(request, 'Doctor/doctorprofile.html', context={'data':data})

def viewappoint(request):
    appointments = Appointment.objects.all().order_by('day')
    return render(request, 'Doctor/viewappointment.html', context={'appointments':appointments})

def user_logout(request):
    logout(request)
    return render(request,'Patient\Main\index.html',context={})

