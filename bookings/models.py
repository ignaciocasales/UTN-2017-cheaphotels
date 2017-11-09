from django.db import models


class City(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)


class Passenger(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=False, null=False, max_length=50)
    email = models.EmailField(blank=False, null=False, max_length=200)


class Property(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    description = models.TextField(blank=False, null=False, default="Awesome description")
    picture = models.ImageField(blank=True, null=True)
    property_number = models.PositiveIntegerField(blank=False, null=False)
    max_pax = models.PositiveIntegerField(blank=False, null=False)
    daily_cost = models.FloatField(blank=False, null=False)
    city = models.OneToOneField(City, on_delete=models.DO_NOTHING, blank=False, null=False)


class Reservation(models.Model):
    reservation_date = models.DateField(blank=False, null=False, auto_now=True)
    reservation_number = models.PositiveIntegerField(blank=False, null=False, unique=True)
    total_amount = models.FloatField(blank=False, null=False)
    passenger = models.OneToOneField(Passenger, on_delete=models.DO_NOTHING, blank=False, null=False)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False)


class ReservationDate(models.Model):
    date = models.DateField(blank=False, null=False)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, blank=False, null=False)
