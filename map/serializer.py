from rest_framework import serializers
from .models import EyeTracking, Locations, SpeedLimits


class EyeTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EyeTracking
        fields = ('x', 'y', 'loc_id')
        # fields = '__all__'
        depth = 1


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('lat', 'lon', 'speed','time')
        depth = 1


class SpeedLimitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedLimits
        fields = ('limit', 'loc_id')
        depth = 2
        # fields = ('id','loc_id','limit')
