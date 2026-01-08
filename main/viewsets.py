from main.models import Actvity, Driver, Trip
from main.serializers import ActivitySerializer, DriverSerializer, TripSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TripViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Trip.objects.all().order_by('-created_at')
    serializer_class = TripSerializer


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Actvity.objects.all()
    serializer_class = ActivitySerializer