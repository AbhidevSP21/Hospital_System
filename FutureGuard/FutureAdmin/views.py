from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .models import Doctor

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

        # Create a new doctor instance and save it to the database
        doctor = Doctor(name=name, specialization=specialization, contact=contact)
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