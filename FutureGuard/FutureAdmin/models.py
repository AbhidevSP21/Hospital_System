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

QUALIFICATION_CHOICES = (
    ("MBBS", "MBBS"),
    ("MD", "MD (Doctor of Medicine)"),
    ("DO", "DO (Doctor of Osteopathic Medicine)"),
    ("MS", "MS (Master of Surgery)"),
    ("DM", "DM (Doctorate of Medicine)"),
    ("MCh", "MCh (Master of Chirurgiae)"),
    ("DNB", "DNB (Diplomate of National Board)"),
    ("BDS", "BDS (Bachelor of Dental Surgery)"),
    ("MDS", "MDS (Master of Dental Surgery)"),
    ("BAMS", "BAMS (Bachelor of Ayurvedic Medicine and Surgery)"),
    ("BHMS", "BHMS (Bachelor of Homeopathic Medicine and Surgery)"),
    ("BPT", "BPT (Bachelor of Physiotherapy)"),
    ("MPT", "MPT (Master of Physiotherapy)"),
    ("PhD", "PhD (Doctor of Philosophy)"),
    ("Fellowship", "Fellowship"),
)


class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=DOCTOR_CATEGORY_CHOICES, default="General Physician")
    qualification = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES, default="MBBS")
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=128)  # Store hashed password
    
    def __str__(self):
        return self.name
