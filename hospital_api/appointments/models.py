from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
from django.conf import settings

# Create your models here.

class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    room = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=20, 
    choices=[('pending', 'Pending'),
             ('confirmed', 'Confirmed'),
             ('cancelled', 'Cancelled'),
             ], 
             default='pending')

