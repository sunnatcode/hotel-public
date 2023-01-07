from .models import Room, RoomStatus, RoomType
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from book.serializers import BookingSerializers


class RoomStatusSerializers(serializers.ModelSerializer):
    def validate(self, validated_data):
        if RoomStatus.objects.filter(status_name=validated_data['status_name']):
            raise ValidationError('This status name already exists')

        return validated_data

    class Meta:
        model = RoomStatus
        fields = ('status_name', 'status_description')


class RoomTypeSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        if RoomType.objects.filter(name=attrs['name']):
            raise ValidationError('This room type already exists')

        return attrs

    class Meta:
        model = RoomType
        fields = ('name', 'max_guest', 'smoking', 'description', 'price')


class RoomSerializers(serializers.ModelSerializer):
    roomtype = RoomTypeSerializers(many=True, read_only=True)
    room_status = RoomStatusSerializers(many=True, read_only=True)
    booking = BookingSerializers(many=True, read_only=True)

    def validate(self, validated_data):
        if Room.objects.filter(room_number=validated_data['room_number']):
            raise ValidationError('This room already exists')

        if Room.objects.filter(floor_number=validated_data['floor_number']):
            raise ValidationError('This floor already exists')

        return validated_data

    class Meta:
        model = Room
        fields = ['room_number', 'floor_number', 'roomtype', 'booking', 'room_status']
