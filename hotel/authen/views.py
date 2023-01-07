from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RegisterUserSerializers, EmployerSerializers, JobSerializers
from .models import Customer, Employer, Jobs
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class RegisterUserView(GenericAPIView):
    serializer_class = RegisterUserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        ser = RegisterUserSerializers(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            data = {
                "status": 201,
                'success': True,
                "data": ser.data
            }
            return Response(data=data)
        return Response(ser.errors)
    
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        ser = RegisterUserSerializers(queryset, many=True)
        return Response(ser.data)

class EmployerView(ModelViewSet):
    permission_classes  = [IsAdminUser]
    serializer_class = EmployerSerializers
    queryset = Employer.objects.all()

    def create(self, request, *args, **kwargs):
        ser = EmployerSerializers(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            data = {
                "status": 201,
                'success': True,
                "data": ser.data
            }
            return Response(data=data)
        return Response(ser.errors)
    
    def list(self, request, *args, **kwargs):
        queryset = Employer.objects.all()
        ser = EmployerSerializers(queryset, many=True)
        return Response(ser.data)

class JobsView(ModelViewSet):
    permission_classes  = [IsAdminUser]
    serializer_class = JobSerializers
    queryset = Jobs.objects.all()

    def create(self, request, *args, **kwargs):
        ser = JobSerializers(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            data = {
                "status": 201,
                'success': True,
                "data": ser.data
            }
            return Response(data=data)
        return Response(ser.errors)
    
    def list(self, request, *args, **kwargs):
        queryset = Jobs.objects.all()
        ser = JobSerializers(queryset, many=True)
        return Response(ser.data)