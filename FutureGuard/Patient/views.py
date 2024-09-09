from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import PatientProfile
from django.contrib.auth.hashers import make_password



def index(request):
    return render(request,"Patient\Main\index.html",context={})

def login_access(request) :
    return render(request, "Patient\Main\login.html",context={})

def doctorlist(request) :
    return render(request, "Patient\Main\doctorlist.html",context={})
def feedback(request) :
    return render(request, "Patient/Main/feedback.html",context={})
def contact(request) :
    return render(request, "Patient\Main\contact.html",context={})
def about(request) :
    return render(request, "Patient/Main/about.html",context={})
def userprofile(request) :
    return render(request, "Patient/Main/userprofile.html",context={})

def patient_register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        password=request.POST['password']
        role='Patient'
        user=User.objects.create_user(username=email)
        user.set_password(password)
        user.save()
        PatientProfile.objects.create(user=user,email=email,name=name,phone_no=phone_no,role=role)

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