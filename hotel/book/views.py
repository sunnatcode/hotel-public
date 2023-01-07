from django.shortcuts import render
from .serializers import BookingSerializers
from .models import Booking
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
# Create your views here.


class BookListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

    def post(self, request, *args, **kwargs):
        ser = BookingSerializers(data=request.data)
        