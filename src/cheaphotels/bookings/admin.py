from django.contrib import admin

from .models import Property, ReservationDate, City


class ReservationDateInline(admin.TabularInline):
    model = ReservationDate
    fk_name = 'property'
    max_num = 7


class AdminProperty(admin.ModelAdmin):
    inlines = [ReservationDateInline, ]


admin.site.register(City)
admin.site.register(Property, AdminProperty)
