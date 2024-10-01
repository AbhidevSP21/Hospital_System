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
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    role=models.CharField(max_length=20,choices=(
        ('patient','Patient'),
        ('doctor','Doctor'),
    ),default='Patient')

class feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    rating=models.IntegerField(null=False)
    feedback=models.CharField(max_length=1000,null=True)