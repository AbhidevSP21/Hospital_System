from django.db import models
from django.contrib.auth.models import User


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
    medical_report = models.FileField(upload_to='medical_docs/', blank=True, null=True)  # PDF upload

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    rating=models.IntegerField(null=False)
    feedback=models.CharField(max_length=1000,null=True)