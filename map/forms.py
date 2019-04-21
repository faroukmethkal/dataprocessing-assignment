from django import forms
from .models import EyeTracking


class EyeTrackingForm(forms.ModelForm):
    class Meta:
        model = EyeTracking
        fields = [
            'loc_id',
            'x',
            'y'
        ]
