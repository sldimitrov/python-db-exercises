from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=40)
    species = models.CharField(max_length=40)


class Artifact(models.Model):
    name = models.CharField(max_length=70)
    origin = models.CharField(max_length=70)
    age = models.IntegerField()
    description = models.TextField()
    is_magical = models.BooleanField()


class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    population = models.IntegerField()
    description = models.TextField()
    is_capital = models.BooleanField(default=False)


class Car(models.Model):
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    color = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Task(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=25)
    description = models.TextField()
    due_date = models.DateField()
    is_finished = models.BooleanField(default=False)


class HotelRoom(models.Model):
    ROOM_TYPES = {
        "STANDARD": "Standard",
        "DELUXE": "Deluxe",
        "SUITE": "Suite"
    }

    room_number = models.IntegerField()
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    amenities = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_reserved = models.BooleanField(default=False)
