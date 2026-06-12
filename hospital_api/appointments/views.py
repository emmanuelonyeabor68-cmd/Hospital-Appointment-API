from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from doctors.models import Doctor

from rest_framework.exceptions import ValidationError

from .models import Appointment
from .serializers import AppointmentSerializer
from datetime import datetime
from rest_framework.decorators import action
from rest_framework.response import Response
from .permission import IsDoctor, IsPatient

# Create your views here.

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'date', 'doctor']
  

    def perform_create(self, serializer):
        user = self.request.user

        if user.role != 'patient':
            raise PermissionDenied("only patient can create appointments")  
        serializer.save(patient=user)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return Appointment.objects.filter(doctor__user=user)
        return Appointment.objects.filter(patient=user)    

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        appointment = self.get_object()

        if request.user.role != 'patient':
            raise PermissionDenied("only patients can cancel")
        if appointment.patient != request.user:
            raise PermissionDenied("not your appointment")
        if appointment.status == 'cancelled':
            return Response({"error": "Already cancelled"}, status=400)
        appointment.status = 'cancelled'
        appointment.save()
        return Response({"message": "Appointment cancelled"})
    
    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        appointment = self.get_object()

        if request.user.role != 'doctor':
            raise PermissionDenied("Only doctors")
        
        if appointment.doctor.user != request.user:
            raise PermissionDenied("Not your patient")

        if appointment.status == 'cancelled':
             return Response({"error": "cannot confirm a cancelled appointment"}, status=400)

        if appointment.status == 'confirmed':
            return Response({"error": "Already confirmed"}, status=400)
        appointment.status = 'confirmed'
        appointment.save()
        return Response({"message": "Appointment confirmed"})
        
        
    

