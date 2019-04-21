from django import forms
from .models import EyeTracking, Locations, SpeedLimits


class EyeTrackingForm(forms.ModelForm):
    class Meta:
        model = EyeTracking
        fields = [
            'loc_id',
            'x',
            'y'
        ]

class LocationsForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = [
            'name',
            'lat',
            'lon',
            'speed',

        ]


class SpeedLimitsForm(forms.ModelForm):
    class Meta:
        model = SpeedLimits
        fields = [
            'loc_id',
            'limit',

        ]