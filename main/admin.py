from django.contrib import admin
from .models import Driver, Trip, Actvity

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('pickup_location', 'dropoff_location', 'driver', 'created_at')  

@admin.register(Actvity)
class ActvityAdmin(admin.ModelAdmin):
    list_display = ('driver', 'activity_type', 'start_time', 'end_time', 'location')
