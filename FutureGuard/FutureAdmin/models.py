from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
