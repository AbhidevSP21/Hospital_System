from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import PatientProfile, feedback
from django.contrib.auth.hashers import make_password
import csv
from django.conf import settings
import os



def index(request):
    review = feedback.objects.all()
    return render(request,"Patient\Main\index.html",{'review':review})

def login_access(request):
    return render(request, "Patient\Main\login.html",context={})

def doctorlist(request) :
    return render(request, "Patient\Main\doctorlist.html",context={})

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

def contact(request) :
    return render(request, "Patient\Main\contact.html",context={})
def about(request) :
    return render(request, "Patient/Main/about.html",context={})

def userprofile(request) :
    data = PatientProfile.objects.filter(user_id = request.user)
    return render(request, "Patient/Main/userprofile.html",{'data':data})
def appointment(request) :
    return render(request, "Patient/Main/appointment.html",context={})

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