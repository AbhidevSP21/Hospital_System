from django.contrib import admin
from .models import PatientProfile, feedback, Appointment

admin.site.register(PatientProfile)
admin.site.register(feedback)
admin.site.register(Appointment)
