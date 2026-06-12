from django.shortcuts import render
from rest_framework import viewsets

from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.permissions import AllowAny,IsAdminUser, IsAuthenticated


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        if self.action in ['update', 'partial_update','destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.action == 'list':
            return Doctor.objects.filter(available=True)
        return Doctor.objects.all()

   
