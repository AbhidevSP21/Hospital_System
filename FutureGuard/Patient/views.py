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

