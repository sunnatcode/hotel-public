from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
from django.contrib.auth import get_user_model
from .models import Customer, Jobs, Employer
from django.db.transaction import atomic


class RegisterUserSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    phone_number = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError('This user already exists')

        if User.objects.filter(email=data['email']).exists():
            raise ValidationError('This email already exists')
        return data

    @atomic
    def create(self, validated_data):
        user = User.objects.create_user(username=self.data['username'],
                                        first_name=self.data['first_name'],
                                        last_name=self.data['last_name'],
                                        email=self.data['email'],
                                        password=self.data['password'])

        return Customer.objects.create(user=user, phone_number=validated_data["phone_number"])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'phone_number', 'last_name', 'password')


class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'
