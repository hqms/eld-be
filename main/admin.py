from django.contrib import admin
from .models import Driver, Trip

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('pickup_location', 'dropoff_location', 'driver', 'created_at')  