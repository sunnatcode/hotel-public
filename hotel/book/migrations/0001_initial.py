# Generated by Django 4.1.4 on 2022-12-29 19:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('checkout_date', models.DateTimeField(default=datetime.datetime(2022, 12, 30, 19, 5, 56, 973311, tzinfo=datetime.timezone.utc))),
                ('check_out', models.BooleanField(default=False)),
                ('no_of_guests', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='rooms.room')),
            ],
        ),
    ]