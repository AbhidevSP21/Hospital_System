# Generated by Django 4.2.7 on 2024-10-01 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='password',
        ),
    ]