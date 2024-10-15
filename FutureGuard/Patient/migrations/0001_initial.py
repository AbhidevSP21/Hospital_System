# Generated by Django 4.2.5 on 2024-10-15 11:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], default='Patient', max_length=20)),
                ('dob', models.DateField(null=True)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('emergency_contact', models.CharField(max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('medical_report', models.FileField(blank=True, null=True, upload_to='medical_docs/')),
                ('prev_checkup', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=1000, null=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Doctor care', 'Doctor care'), ('Nursing care', 'Nursing care'), ('Medical social services', 'Medical social services'), ('Homemaker or basic assistance care', 'Homemaker or basic assistance care')], default='Doctor care', max_length=50)),
                ('doctor_category', models.CharField(choices=[('General Physician', 'General Physician'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Orthopedics', 'Orthopedics'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology'), ('Gynecology', 'Gynecology'), ('Psychiatry', 'Psychiatry')], default='General Physician', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM')], default='3 PM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
