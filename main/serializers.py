from main.models import Trip
from rest_framework import serializers

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id','current_location', 'pickup_location', 'dropoff_location', 'estimated_cycle_used', 'driver', 'created_at']