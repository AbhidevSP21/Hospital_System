from django.contrib import admin
from .models import PatientProfile, feedback

# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(feedback)