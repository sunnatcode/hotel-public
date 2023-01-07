from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import RoomSerializers, RoomStatusSerializers, RoomTypeSerializers
from .models import RoomType, Room, RoomStatus
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
# Create your views here.


class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    # permission_classes = [IsAdminUser]
    serializer_class = RoomSerializers

    def post(self ,request, *args, **kwargs):
        serialier = RoomSerializers(data=request.data)
        if serialier.is_valid(raise_exception=True):
            serialier.save()
            data = {
                "status": 201,
                'success': True,
                'data': serialier.data
            }
            return Response(data)
        return Response({"error": serialier.errors})

    def get(self, request, *args, **kwargs):
        data = Room.objects.all()
        ser = RoomSerializers(data, many=True)
        return Response(ser.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Data deleted'})

class RoomTypeView(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = RoomTypeSerializers

    def post(self ,request, *args, **kwargs):
        serialier = RoomTypeSerializers(data=request.data)
        if serialier.is_valid(raise_exception=True):
            serialier.save()
            return Response(serialier.data)
        return Response({"error": serialier.errors})

    def get(self, request, *args, **kwargs):
        data = RoomType.objects.all()
        ser = RoomTypeSerializers(data, many=True)
        return Response(ser.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Data deleted'})

class RoomStatusView(viewsets.ModelViewSet):
    queryset = RoomStatus.objects.all()
    permission_classess = [IsAdminUser]
    serializer_class = RoomStatusSerializers

    def post(self ,request, *args, **kwargs):
        serialier = RoomStatusSerializers(data=request.data)
        if serialier.is_valid(raise_exception=True):
            serialier.save()
            return Response(serialier.data)
        return Response({"error": serialier.errors})

    def get(self, request, *args, **kwargs):
        data = RoomStatus.objects.all()
        ser = RoomStatusSerializers(data, many=True)
        return Response(ser.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Data deleted'})

class RoomListView(ListAPIView):
    serializer_class  = RoomSerializers
    queryset = Room.objects.all()
    permission_classes = [AllowAny]


