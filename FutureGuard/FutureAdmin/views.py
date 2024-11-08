from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Doctor
from django.db.models import Count
from Patient.models import Appointment,PatientProfile

from django.contrib import messages

# Admin Dashboard View
def admindashboard(request):
    
    # service_b_count = Patient_Appointment.objects.filter(service='Service B').count()
    # service_c_count = Patient_Appointment.objects.filter(service='Service C').count()
    # Add more services as needed

   
    total_doctors = Doctor.objects.count()  # Get total number of doctors
    total_patients = PatientProfile.objects.count()
    
    #total_appointments = Appointment.objects.count()  # Get total number of appointments
    service_a_count =Appointment.objects.filter(service='Dermatology').count()
    service_b_count =Appointment.objects.filter(service='Allergy and Immunology').count()
    service_c_count =Appointment.objects.filter(service='Gastroenterology').count()
    service_d_count =Appointment.objects.filter(service='Endocrinology').count()
    service_e_count =Appointment.objects.filter(service='Pulmonology').count()
    service_f_count =Appointment.objects.filter(service='Cardiology').count()
    service_g_count =Appointment.objects.filter(service='Neurology').count()
    service_h_count =Appointment.objects.filter(service='Infectious Disease').count()
    service_i_count =Appointment.objects.filter(service='Hematology').count()
    service_j_count =Appointment.objects.filter(service='Hepatology').count()
    service_k_count =Appointment.objects.filter(service='Orthopedics').count()
    service_l_count =Appointment.objects.filter(service='Urology').count()
    service_m_count =Appointment.objects.filter(service='Proctology').count()
    service_n_count =Appointment.objects.filter(service='Vascular Surgery').count()
    
    appoint=Appointment.objects.all().count()
    context = {
        'total_doctors': total_doctors,
        'service_a_count': service_a_count,
        'service_b_count': service_b_count,
        'service_c_count': service_c_count,
        'service_d_count': service_d_count,
        'service_e_count': service_e_count,
        'service_f_count': service_f_count,
        'service_g_count': service_g_count,
        'service_h_count': service_h_count,
        'service_i_count': service_i_count,
        'service_j_count': service_j_count,
        'service_k_count': service_k_count,
        'service_l_count': service_l_count,
        'service_m_count': service_m_count,
        'service_n_count': service_n_count,
        'total_appointments': appoint,
        'total_patients':total_patients,
    }
    return render(request, 'Admin/MainAdmin/bDbAdmin.html', context)

# Appointments View
# def adminappointments(request):
#     return render(request, 'Admin/MainAdmin/bAptAdmin.html')

# Doctors View
def admindoctors(request):
    doctors = Doctor.objects.all()  # Fetch all doctors from the database
    context = {
        'doctors': doctors,
    }
    return render(request, 'Admin/MainAdmin/bDrAdmin.html', context)

# Patients View
def adminpatients(request):
    patients = PatientProfile.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'Admin/MainAdmin/bPtAdmin.html',{'patients':patients})

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
        doctor.email = request.POST.get('email')
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


def adminappointments(request):
    appoint=Appointment.objects.all()
  
    return render(request,'Admin/MainAdmin/bAptAdmin.html',{'appoint':appoint})

def delete_patient(request, patient_id):
    patient = get_object_or_404(PatientProfile, id=patient_id)  # Fetch doctor by ID
    patient.user.delete()  # Delete associated user
    patient.delete()  # Delete the patient

    return redirect('adminpatients')  # Redirect to patients page