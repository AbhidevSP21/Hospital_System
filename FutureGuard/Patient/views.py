from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"Patient\Main\index.html",context={})

def login(request) :
    return render(request, "Patient\Main\login.html",context={})

def doctorlist(request) :
    return render(request, "Patient\Main\doctorlist.html",context={})
def feedback(request) :
    return render(request, "Patient/Main/feedback.html",context={})
def contact(request) :
    return render(request, "Patient\Main\contact.html",context={})
def about(request) :
    return render(request, "Patient/Main/about.html",context={})
def portal(request) :
    return render(request, "Patient\Main\Portal.html",context={})
def appointment(request) :
    return render(request, "Patient/Main/appointment.html",context={})
def prediction(request) :
    return render(request, "Patient\Main\Prediction.html",context={})


