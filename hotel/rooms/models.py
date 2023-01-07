from django.db import models


# Create your models here.


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    max_guest = models.IntegerField()
    smoking = models.BooleanField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class RoomStatus(models.Model):
    status_name = models.CharField(max_length=100)
    status_description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.status_name


class Room(models.Model):
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    is_available = models.BooleanField(default=True)
    roomtype = models.ManyToManyField(RoomType)
    room_status = models.ManyToManyField(RoomStatus)

    @property
    def reservations(self):
        return self.booking.all()

    def __str__(self) -> str:
        return self.room_number
