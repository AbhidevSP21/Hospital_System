from django.shortcuts import render, redirect


def admindashboard(request):
    return render(request, 'Admin/MainAdmin/bDbAdmin.html',context={})

def adminappointments(request):
    return render(request, 'Admin/MainAdmin/bAptAdmin.html',context={})

def admindoctors(request):
    return render(request, 'Admin/MainAdmin/bDrAdmin.html',context= {})

def adminpatients(request):
    return render(request, 'Admin/MainAdmin/bPtAdmin.html',context={})

def adminsettings(request):
    return render(request, 'Admin/MainAdmin/bSetAdmin.html',context={})