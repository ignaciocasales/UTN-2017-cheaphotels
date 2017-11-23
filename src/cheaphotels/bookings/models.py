import os
from django.db import models


def property_image_rename(instance, filename):
    path = "hotels/images/"
    if instance.id is not None:
        name = str(instance.id) + filename
    elif not Property.objects.last():
        name = str(1) + filename
    else:
        name = str(Property.objects.latest('id').pk + 1) + filename
    return os.path.join(path, name)


class City(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Passenger(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=False, null=False, max_length=50)
    email = models.EmailField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.first_name + '' + self.last_name


class Property(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, default="Property Name")
    description = models.TextField(blank=False, null=False, default="Awesome description")
    picture = models.ImageField(blank=True, null=True, upload_to=property_image_rename)
    max_pax = models.PositiveIntegerField(blank=False, null=False, default=1)
    daily_cost = models.FloatField(blank=False, null=False, default=0)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=False, null=False)

    class Meta:
        verbose_name_plural = "properties"

    def __str__(self):
        return self.name


class Reservation(models.Model):
    reservation_date = models.DateField(blank=False, null=False, auto_now=True)
    reservation_number = models.PositiveIntegerField(blank=False, null=False, unique=True)
    total_amount = models.FloatField(blank=False, null=False)
    passenger = models.OneToOneField(Passenger, on_delete=models.DO_NOTHING, blank=False, null=False)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.property.name + ' | ' + self.passenger.first_name + ' ' + self.passenger.last_name


class ReservationDate(models.Model):
    date = models.DateField(blank=False, null=False)
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False)
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.property.name
