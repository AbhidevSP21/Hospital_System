from django.shortcuts import render

# Create your views here.
def doctor_profile(request):
    return render(request, 'Doctor/doctorprofile.html', context={})