from main.models import Trip
from main.serializers import TripSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TripViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Trip.objects.all().order_by('-created_at')
    serializer_class = TripSerializer