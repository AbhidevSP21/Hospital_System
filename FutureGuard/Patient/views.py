from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import PatientProfile, feedback, Prediction
from django.contrib.auth.hashers import make_password
import csv
from django.conf import settings
import os
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
import joblib
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder as le



def index(request):
    review = feedback.objects.all()
    return render(request,"Patient\Main\index.html",{'review':review})

def login_access(request):
    return render(request, "Patient\Main\login.html",context={})

def doctorlist(request) :
    return render(request, "Patient\Main\doctorlist.html",context={})

def profileupdate(request):
    if request.method == 'POST':
        # Retrieve user profile, return 404 if it does not exist
        profile = get_object_or_404(PatientProfile, user=request.user)

        # Extract form data
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        emergency_contact = request.POST.get('emergency_contact')
        profile_picture = request.FILES.get('profile_picture')
        medical_report = request.FILES.get('medical_report')

        # Update profile fields if they are provided
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
            # print(profile.profile_picture)
        if medical_report:
            profile.medical_report = medical_report

        # Save the profile
        profile.save()

        # Display a success message
        messages.success(request, "Profile updated successfully.")

        # Redirect to the profile page or another page as needed
        return redirect('userprofile')  # Replace 'profile_view' with the appropriate URL name

    # Render the profile update template with context if needed
    return render(request, "Patient/Main/Profile_Update.html")

def editprofile(request) :
    # update=PatientProfile.objects.all()
    return render(request, "Patient\Main\editprofile.html")

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
    #update=MedicalProfile.objects.all()
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

from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Appointment  # Make sure to import your Appointment model

def booking(request):

    if request.method == 'POST':


        service = request.POST['service']
        user = request.user
        date = request.POST['day']

        appoinment=Appointment(
                                    user=user,
                                    service=service,
                                    day=date
                            )
        appoinment.save()
        messages.success(request, "Appointment Saved!")
        return redirect('userprofile')
    else:
        return render(request, 'Patient/Main/appointment.html', context={})



def contact(request) :
    return render(request, "Patient\Main\contact.html",context={})
def about(request) :
    return render(request, "Patient/Main/about.html",context={})

def userprofile(request) :
    data = PatientProfile.objects.filter(user_id = request.user)
    appoint = Appointment.objects.filter(user_id = request.user).order_by('-day')[:5]
    prediction = Prediction.objects.filter(user_id = request.user)
    context={'data':data,'appoint':appoint, 'prediction':prediction}
    # print(context)
    return render(request, "Patient/Main/userprofile.html",context=context)

def prediction(request):


    # Define the path to your CSV file
    csv_path = settings.DATA_DIR / 'symptoms.csv'
    symptoms = []

    # Read symptoms from the CSV file
    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                symptoms.append(row[0])  # Assuming each symptom is in the first column
    except FileNotFoundError:
        return render(request, "Patient/Main/Prediction.html", {'msg': "Error: Symptoms file not found."})

    # Prepare default values for context
    precautions = {}
    msg = ""

    # Handle form submission
    if request.method == 'POST':


        selected_symptoms = request.POST.getlist('symptoms')
        test_case = np.zeros(len(symptoms))  # Initialize all symptoms to False (0)
        
        for symptom in selected_symptoms:
            if symptom in symptoms:
                test_case[symptoms.index(symptom)] = 1  # Set True (1) for specified symptoms

        # Reshape for prediction
        test_case = test_case.reshape(1, -1)
        
        try:
            # Load the prediction model and label encoder
            preds = load_model("Data\Model\prediction.h5")
            le = joblib.load("Data\Model\le.joblib")
            
            # Perform prediction
            predicted_disease_prob = preds.predict(test_case)
            disease_index = np.argmax(predicted_disease_prob)
            predicted_disease = le.inverse_transform([disease_index])[0]
            
            msg = f"Predicted Disease: {predicted_disease}. Please consult the doctor for further checkup." 
            
            # Retrieve precautions for the predicted disease
            with open("Data\Model\symptom_precaution.csv", 'r', newline='', encoding='utf-8') as file:
                reader1 = csv.DictReader(file, delimiter=',')
                for row in reader1:
                    if row['Disease'].strip().lower() == predicted_disease.strip().lower():
                        precautions = {
                            'precaution1': row.get('Precaution_1'),
                            'precaution2': row.get('Precaution_2'),
                            'precaution3': row.get('Precaution_3'),
                            'precaution4': row.get('Precaution_4'),
                        }
                        break

        except FileNotFoundError:
            msg = "Error: Model or precaution file not found."
        except TypeError as e:
            msg = f"Error: {str(e)}"
        
        user_id=request.user.id
        user=User.objects.get(id=user_id)
        prediction_record = Prediction(user=user, predicted_disease=predicted_disease)
        prediction_record.save()
    
    # Render the form and pass precautions and symptoms data
    return render(request, "Patient/Main/Prediction.html", {'symptoms': symptoms, 'msg': msg, 'precautions': precautions})


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
            if user.is_superuser == False and user.is_staff == False:
                login(request, user)
                return redirect('userprofile') 
            
            elif user.is_superuser == False and user.is_staff == True:
                login(request, user)
                return redirect('doctor_profile')  # redirect to 'userprofile' view
            
            elif user.is_superuser == True and user.is_staff == True:
                login(request, user)
                return redirect('admindashboard')  # redirect to 'userprofile' view
        
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
