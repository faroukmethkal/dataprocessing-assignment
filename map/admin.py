from django.contrib import admin
from .models import Locations, SpeedLimits, EyeTracking

admin.site.register(SpeedLimits)
admin.site.register(Locations)
admin.site.register(EyeTracking)
