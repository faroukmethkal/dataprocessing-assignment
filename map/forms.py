from django import forms
from .models import EyeTracking, Locations


class EyeTrackingForm(forms.ModelForm):
    class Meta:
        model = EyeTracking
        fields = [
            'loc_id',
            'x',
            'y'
        ]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = [
            'name',
            'lat',
            'lon',
            'speed',
            'time'


        ]
