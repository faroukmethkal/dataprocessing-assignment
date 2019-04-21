from django.shortcuts import render
from django.views.generic import View
from .models import Locations, SpeedLimits, EyeTracking
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EyeTrackingSerializer, LocationsSerializer, SpeedLimitsSerializer
from .forms import EyeTrackingForm


def index(request):
    return render(request,'map/index.html')


def showmap(request):
    locations = Locations.objects.all()
    return render(request, 'map/showmap.html', {'locations': locations})


def eye_tracking(request):
    form = EyeTrackingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EyeTrackingForm()
    context = {
        'form': form,
    }
    return render(request, 'map/formEyeTracking.html', context)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'map/home.html', {})


class ChartEyeTraking(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        eyetracking = EyeTracking.objects.select_related('loc_id').all()
        # print(eyetracking[0].loc_id.lat, eyetracking[0].loc_id.lon)
        for eye in eyetracking:
            print(eye.loc_id.lat, eye.loc_id.lon)
        serializers = EyeTrackingSerializer(eyetracking, many=True)
        return Response(serializers.data)


class SpeedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'map/speedchart.html', {})


class ChartSpeed(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        speed = SpeedLimits.objects.all()
        serializers = SpeedLimitsSerializer(speed, many=True)
        return Response(serializers.data)














# from django.http import JsonResponse
# from django.core import serializers
# from django.contrib.auth import get_user_model


# def home(request):
#     obj1 = Locations.objects.all()
#     obj2 = SpeedLimits.objects.all()
#     context = {
#         'object1': obj1,
#         'object2': obj2
#     }
#     return render(request, 'map/home.html', context)


# def speedchart(request):
#     obj1 = Locations.objects.all()
#     obj2 = SpeedLimits.objects.all()
#     context = {
#         'object1': obj1,
#         'object2': obj2
#     }
#     return render(request, 'map/speedchart.html', context)

#
# def focuse(request):
#     obj1 = EyeTracking.objects.all()
#
#     return render(request, 'map/focuse.html', {'object1': obj1})
#
#


# locations = Rulelocation.objects.all()
# return render(request, 'map/home.html', {'locations': locations})
# query_validation = Location.objects.all()
# validation = serializers.serialize('json', query_validation)
# print(validation)
# return render(request, 'map/home.html', {'validation': validation})

# obj1 = Location.objects.get(id=1)
# obj2 = Rulelocation.objects.get(id=1)
# context = {
#     'object1':obj1,
#     'object2':obj2
# }
# return render(request, 'map/home.html', context)
# locations = Location.objects.all()
# roleLocation = Rulelocation.objects.all()
# return render(request, 'map/home.html', {'locations': locations, 'roleLocation': roleLocation})
# query_validation = Location.objects.all()
# print(query_validation)
# validation = serializers.serialize('json', query_validation)
# print(validation)
# return render(request, 'map/home.html', {'validation': validation})


# print(q)
# default_item = [12,12,-12,2]
# data = {
#     "default": default_item,
# }
# return Response(data)
# # return JsonResponse(serializers.serialize('json', data), safe=False)
