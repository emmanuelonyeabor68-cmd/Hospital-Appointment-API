from rest_framework import serializers
from django.contrib.auth import get_user_model
from doctors.models import Doctor

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    speciality = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'speciality']

    def create(self, validated_data):
        speciality = validated_data.pop('speciality', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 'patient')
        )
        if user.role == 'doctor':
            if not speciality:
                raise serializers.ValidationError("Doctors must provide speciality")
            Doctor.objects.create(user=user, speciality=speciality)


        return user