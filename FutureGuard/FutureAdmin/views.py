from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Doctor

# Admin Dashboard View
def admindashboard(request):
    total_doctors = Doctor.objects.count()  # Get total number of doctors
    context = {
        'total_doctors': total_doctors,
    }
    return render(request, 'Admin/MainAdmin/bDbAdmin.html', context)

# Appointments View
def adminappointments(request):
    return render(request, 'Admin/MainAdmin/bAptAdmin.html')

# Doctors View
def admindoctors(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    context = {
        'doctors': doctors,
    }
    return render(request, 'Admin/MainAdmin/bDrAdmin.html', context)

# Patients View
def adminpatients(request):
    return render(request, 'Admin/MainAdmin/bPtAdmin.html')

# Admin Settings View
def adminsettings(request):
    return render(request, 'Admin/MainAdmin/bSetAdmin.html')

# Logout View
def adminlogout(request):
    logout(request)  # Logout the user
    return redirect("index")  # Redirect to the home page

# Add Doctor View
def add_doctor(request):
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('doctorName')
        specialization = request.POST.get('specialization')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create and hash the password
        hashed_password = make_password(password)

        # Create a new user and assign it to the doctor
        user = User.objects.create(
            first_name=name, 
            username=email, 
            email=email, 
            password=hashed_password, 
            is_staff=True
        )

        # Save the doctor with the associated user
        doctor = Doctor.objects.create(
            user=user,
            specialization=specialization,
            contact=contact,
            email=email
        )

        return redirect('admindoctors')  # Redirect to the doctors page

    return render(request, 'Admin/MainAdmin/bDrAdmin.html')

# Edit Doctor View
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Fetch doctor by ID

    if request.method == 'POST':
        # Update doctor details with form data
        doctor.user.first_name = request.POST.get('doctorName')
        doctor.specialization = request.POST.get('specialization')
        doctor.contact = request.POST.get('contact')
        doctor.user.save()  # Save changes to User model
        doctor.save()  # Save changes to Doctor model

        return redirect('admindoctors')  # Redirect to doctors page

    context = {'doctor': doctor}
    return render(request, 'Admin/MainAdmin/editDoctor.html', context)

# Delete Doctor View
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Fetch doctor by ID
    doctor.user.delete()  # Delete associated user
    doctor.delete()  # Delete the doctor

    return redirect('admindoctors')  # Redirect to doctors page
