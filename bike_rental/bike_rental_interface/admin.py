from django.contrib import admin

# bike_rental/admin.py
from django.contrib import admin
from .models import BikeRentalBike, BikeRentalTransaction

admin.site.register(BikeRentalBike)
admin.site.register(BikeRentalTransaction)


# Register your models here.
