from django.db import models
from django.contrib.auth.models import User

DOCTOR_CATEGORY_CHOICES = (
    ("General Physician", "General Physician"),
    ("Cardiology", "Cardiology"),
    ("Neurology", "Neurology"),
    ("Orthopedics", "Orthopedics"),
    ("Pediatrics", "Pediatrics"),
    ("Dermatology", "Dermatology"),
    ("Gynecology", "Gynecology"),
    ("Psychiatry", "Psychiatry"),
)

class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    specialization = models.CharField(max_length=50, choices=DOCTOR_CATEGORY_CHOICES, default="General Physician")
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=128)  # Store hashed password
    
    def __str__(self):
        return self.name
