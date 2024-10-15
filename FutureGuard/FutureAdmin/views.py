from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Doctor
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def admindashboard(request):
    return render(request, 'Admin/MainAdmin/bDbAdmin.html',context={})

def adminappointments(request):
    return render(request, 'Admin/MainAdmin/bAptAdmin.html',context={})

def admindoctors(request):
    doctors = Doctor.objects.all()
    
    context = {
        "doctors" : doctors
    }
    
    return render(request, 'Admin/MainAdmin/bDrAdmin.html',context)

def adminpatients(request):
    return render(request, 'Admin/MainAdmin/bPtAdmin.html',context={})

def adminsettings(request):
    return render(request, 'Admin/MainAdmin/bSetAdmin.html',context={})

def adminlogout(request):
    logout(request)
    return redirect("index")


def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('doctorName')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')

        hashed_password = make_password(password)
        
        user = User.objects.create(first_name=name, username=email,email=email,password=hashed_password,is_staff=True)
        doctor = Doctor(user=user, specialization=specialization, contact=contact, email=email, password=password)
        doctor.save()

        return redirect('admindoctors')  # Redirect to the doctor page after saving

    return render(request, 'Admin/MainAdmin/bDrAdmin.html')

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Get the doctor by ID

    if request.method == 'POST':
        doctor.name = request.POST.get('doctorName')  # Update the name
        doctor.specialization = request.POST.get('specialization')  # Update specialization
        doctor.contact = request.POST.get('contact')  # Update contact
        doctor.save()  # Save changes to the database

        return redirect(admindoctors)  # Redirect to the doctor page after saving

    return render(request, 'Admin/MainAdmin/editDoctor.html', {'doctor': doctor})

def delete_doctor(request, doctor_id):
    dr = Doctor.objects.get(id = doctor_id)
    dr.delete()
    return redirect(admindoctors)