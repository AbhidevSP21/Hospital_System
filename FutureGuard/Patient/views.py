from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from .models import user_details, interests, improvements,teching,feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request,"Patient/Main/index.html")
