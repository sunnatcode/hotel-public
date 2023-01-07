from django.db import models
from django.utils import timezone

from rooms.models import Room
from authen.models import Customer
from django.db import models
from datetime import datetime, date, timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now


class Guest(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def __str__(self):
        return str(self.room_no)

    def hotel_name(self):
        return self.hotel.name


class Booking(models.Model):
    # guest_name=models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(default=timezone.now)
    checkout_date = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    check_out = models.BooleanField(default=False)
    no_of_guests = models.IntegerField(default=1)

    def charge(self):
        if self.check_out:
            if self.checkin_date == self.checkout_date:
                return self.room.rate
            else:
                time_delta = self.checkout_date - self.checkin_date
                total_time = time_delta.days
                total_cost = total_time * self.room.rate
                # return total_cost
                return total_cost
        else:
            return 'calculated when checked out'
