from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Booking


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'