from django.contrib import admin
from .models import PatientProfile, feedback, Appointment  # Updated to Feedback

# Register your models here
admin.site.register(PatientProfile)
admin.site.register(feedback)  # Register Feedback model
admin.site.register(Appointment)
