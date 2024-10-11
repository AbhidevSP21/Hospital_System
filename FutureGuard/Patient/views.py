from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import PatientProfile, feedback
from django.contrib.auth.hashers import make_password
import csv
from django.conf import settings
import os
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages



def index(request):
    review = feedback.objects.all()
    return render(request,"Patient\Main\index.html",{'review':review})

def login_access(request):
    return render(request, "Patient\Main\login.html",context={})

def doctorlist(request) :
    return render(request, "Patient\Main\doctorlist.html",context={})
def profileupdate(request) :
    return render(request, "Patient\Main\Profile_Update.html",context={})

def editprofile(request) :
    if request.method== 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        blood_group=request.POST.get('blood_group')
        emergency_contact=request.POST.get('emergency_contact')
        profile_picture=request.FILES.get('image')
        medical_report=request.FILES.get('doc')

        # if 'phone' in request.POST and request.POST['phone'] is not None:
        #     phone=request.POST['phone']
        #     if PatientProfile.objects.filter(user=request.user,phone_no=phone).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,phone_no=phone)
        #         profile.save()
        # if 'dob' in request.POST and request.POST['dob'] is not None:
        #     dob=request.POST['dob']
        #     if PatientProfile.objects.filter(user=request.user,dob=dob).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,dob=dob)
        #         profile.save()
        # if 'blood_group' in request.POST and request.POST['blood_group'] is not None:
        #     dob=request.POST['blood_group']
        #     if PatientProfile.objects.filter(user=request.user,blood_group=blood_group).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,blood_group=blood_group)
        #         profile.save()
        # if 'emergency_contact' in request.POST and request.POST['emergency_contact'] is not None:
        #     emergency_contact=request.POST['emergency_contact']
        #     if PatientProfile.objects.filter(user=request.user,emergency_contact=emergency_contact).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,emergency_contact=emergency_contact)
        #         profile.save()
        # if 'profile_picture' in request.POST and request.POST['profile_picture'] is not None:
        #     image=request.POST['image']
        #     if PatientProfile.objects.filter(user=request.user,profile_picture=profile_picture).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,profile_picture=profile_picture)
        #         profile.save()
        # if 'medical_report' in request.POST and request.POST['medical_report'] is not None:
        #     image=request.POST['medical_report']
        #     if PatientProfile.objects.filter(user=request.user,medical_report=medical_report).exists():
        #         pass
        #     else:
        #         profile=PatientProfile.objects.create(user=request.user,medical_report=medical_report)
        #         profile.save()
        

        # Get or create a patient profile for the current user
        profile, created = PatientProfile.objects.get_or_create(user=request.user)

        # Update profile fields if they are present in the request
        if phone:
            profile.phone_no = phone
        if dob:
            profile.dob = dob
        if blood_group:
            profile.blood_group = blood_group
        if emergency_contact:
            profile.emergency_contact = emergency_contact
        if profile_picture:
            profile.profile_picture = profile_picture
        if medical_report:
            profile.medical_report = medical_report

        # Save the updated profile
        profile.save()

        # Additional actions (e.g., redirect or render response) can be added here




    #     MedicalProfile.objects.create(
    #         name=name,
    #         email=email,
    #         phone=phone,
    #         dob=dob,
    #         blood_group=blood_group,
    #         emergency_contact=emergency_contact,
    #         profile_picture=profile_picture,
    #         medical_report=medical_report

    #     )
    # update=MedicalProfile.objects.all()
    return render(request, "Patient\Main\editprofile.html",{'update':update})
def viewprofile(request):
    

    return render(request,"Patient/Main/viewprofile.html", context={})

def Patient_feedback(request) :
    if request.method=="POST":
        user_id=request.user.id
        user=User.objects.get(id=user_id)
        name=request.POST['name']
        email=request.POST['email']
        feedback_txt=request.POST['feedback']
        rating=request.POST['rating']
        Feedback=feedback.objects.create(user=user,email=email,name=name,feedback=feedback_txt,rating=rating)
        Feedback.save()
        return redirect('index')
    data = PatientProfile.objects.filter(user_id = request.user)
    return render(request, "Patient/Main/feedback.html",{'data':data})

def booking(request):
    user = request.user
    weekdays = validWeekday(22)  # Calling 'validWeekday' Function to Loop days you want in the next 21 days
    validateWeekdays = isWeekdayValid(weekdays)  # Only show the days that are not full

    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Get stored data from django session (if exists):
    day = request.session.get('day')
    service = request.session.get('service')

    if request.method == 'POST':
        # First step: Selecting service and day
        if not service or not day:
            service = request.POST.get('service')
            day = request.POST.get('day')
            if service is None:
                messages.success(request, "Please Select A Service!")
                return redirect('booking')

            # Store day and service in django session:
            request.session['day'] = day
            request.session['service'] = service

            # Redirect to the same view (second step: confirming time)
            return redirect('booking')

        # Second step: Selecting time and confirming appointment
        else:
            time = request.POST.get("time")
            date = dayToWeekday(day)

            if service:
                if minDate <= day <= maxDate:
                    if date in ['Monday', 'Saturday', 'Wednesday']:
                        if Appointment.objects.filter(day=day).count() < 11:
                            if Appointment.objects.filter(day=day, time=time).count() < 1:
                                AppointmentForm = Appointment.objects.get_or_create(
                                    user=user,
                                    service=service,
                                    day=day,
                                    time=time,
                                )
                                messages.success(request, "Appointment Saved!")
                                return redirect('index')
                            else:
                                messages.success(request, "The Selected Time Has Been Reserved Before!")
                        else:
                            messages.success(request, "The Selected Day Is Full!")
                    else:
                        messages.success(request, "The Selected Date Is Incorrect")
                else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
            else:
                messages.success(request, "Please Select A Service!")

    # Ensure the times list is always passed to the template
    hour = checkTime(times, day) if day else times
    return render(request, 'Patient/Main/appointment.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'times': times,  # Pass the full times list to the template
    })

def contact(request) :
    return render(request, "Patient\Main\contact.html",context={})
def about(request) :
    return render(request, "Patient/Main/about.html",context={})

def userprofile(request) :
    data = PatientProfile.objects.filter(user_id = request.user)
    return render(request, "Patient/Main/userprofile.html",{'data':data})

def prediction(request):
    # Define the path to your CSV file
    # csv_path = os.path.join(settings.BASE_DIR, 'Data', 'symptoms.csv')
    # Using the Data directory path in another part of your project
    csv_path = settings.DATA_DIR / 'symptoms.csv'

    symptoms = []

    # Read symptoms from the CSV file
    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            symptoms.append(row[0])  # Assuming each symptom is in the first column

    # Handle form submission
    if request.method == 'POST':
        selected_symptoms = request.POST.getlist('symptoms')
        # Process selected_symptoms for prediction
        # result = predict_disease(selected_symptoms)
        # Pass result to template or redirect

    return render(request, "Patient/Main/Prediction.html",{'symptoms': symptoms})

def patient_register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        if User.objects.filter(username=email).exists():
            msg = 'username already exists!'
            return render(request, 'Patient/Main/login.html',{'msg':msg})
        else:
            password=request.POST['password']
            role='Patient'
            user=User.objects.create_user(username=email,email=email,first_name=firstname,last_name=lastname)
            user.set_password(password)
            user.save()
            PatientProfile.objects.create(user=user,role=role)

        login(request,user)

        return redirect('login')
    return render(request,"{% url 'user_login' %}")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            # Redirect based on user role
            if user.is_superuser == False and user.is_staff == True:
                login(request, user)
                return redirect('index')  # redirect to the 'index' view
            
            elif user.is_superuser == False and user.is_staff == False:
                login(request, user)
                return redirect('userprofile')  # redirect to 'userprofile' view
        
        else:
            # Wrong credentials or inactive user
            msg = "Wrong credentials. Please try again!"
            return render(request, 'Patient/Main/login.html', {'msg': msg})
    
    # For GET request or if not logged in, show the login page
    return render(request, 'Patient/Main/login.html')
    

def user_logout(request):
    logout(request)
    return redirect('index')

def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
