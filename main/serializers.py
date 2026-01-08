from main.models import Actvity, Driver, Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id','current_location', 'pickup_location', 'dropoff_location', 'estimated_cycle_used', 'driver', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Actvity
        fields = ['id', 'driver', 'activity_type', 'start_time', 'end_time', 'location']    


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'user', 'license_number']