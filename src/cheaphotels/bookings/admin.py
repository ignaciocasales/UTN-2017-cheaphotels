from django.contrib import admin

from .models import Property
from .models import City

# Register your models here.

admin.site.register(City)
admin.site.register(Property)
