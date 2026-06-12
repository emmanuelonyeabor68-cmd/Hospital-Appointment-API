from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="doctor_profile")
    speciality = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    room = models.CharField(max_length=5)

    

    def __str__(self):
        return self.user.username
