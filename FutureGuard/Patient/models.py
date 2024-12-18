from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from FutureAdmin.models import Doctor


# Create your models here.
# class user(User):
#     ROLES = (
#         ('patient','Patient'),
#         ('doctor','Doctor'),
#     )
#     role=models.CharField(max_length=20,choices=ROLES,default='Patient')

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15)
    role=models.CharField(max_length=20,choices=(
        ('patient','Patient'),
        ('doctor','Doctor'),
    ),default='Patient')
    dob = models.DateField(null=True)
    blood_group = models.CharField(max_length=3, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), 
                                                          ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), 
                                                          ('AB+', 'AB+'), ('AB-', 'AB-')],null=True)
    emergency_contact = models.CharField(max_length=15,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    medical_report = models.FileField(upload_to='medical_docs/', blank=True, null=True)
    prev_checkup = models.DateField(null=True)

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    rating=models.IntegerField(null=False)
    feedback=models.CharField(max_length=1000,null=True)



SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
)

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

# Choices for Doctor Category
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

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, default="Doctor care")
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateTimeField(default=datetime.now)
    booking_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"
    
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    predicted_disease = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.predicted_disease} on {self.created_at}"

class Disease(models.Model):
    disease_name = models.CharField(max_length=255,null=True)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.disease_name} - {self.department}"
