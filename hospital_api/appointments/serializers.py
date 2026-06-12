from rest_framework import serializers
from .models import Appointment
from datetime import date

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ['patient']

    def validate(self, data):
        doctor = data["doctor"]
        date = data["date"]
        time = data["time"]

        if not doctor.available:
            raise serializers.ValidationError("This doctor is not available")

        if Appointment.objects.filter(doctor=doctor,date=date,time=time).exists():
            raise serializers.ValidationError("This slot is already booked") 
        return data 
    
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Cannot book past date") 
        return value
    
    
       
        