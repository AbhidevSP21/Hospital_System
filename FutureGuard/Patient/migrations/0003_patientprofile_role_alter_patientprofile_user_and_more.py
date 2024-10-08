# Generated by Django 4.2.7 on 2024-09-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient', '0002_alter_patientprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], default='Patient', max_length=20),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
