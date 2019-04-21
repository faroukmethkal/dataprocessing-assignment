
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import map.views
from django.conf.urls import url
from map.views import ChartEyeTraking, SpeedView, ChartSpeed, HomeView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',map.views.index, name='index'),
    path('showmap/', map.views.showmap, name='showmap'),
    path('eyetracking/', map.views.eye_tracking, name='eyetracking'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ChartEyeTraking.as_view()),


    url(r'^speed/$', SpeedView.as_view(), name='speed'),
    url(r'^api/speed/data/$', ChartSpeed.as_view()),

 ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






# url(r'^api/map/$', ChartSpeed.as_view()),
# url(r'^api/map/$', ChartEyeTraking.as_view()),
# path('',map.views.home, name='home'),
# path('speedchart/',map.views.speedchart,name='speedchart'),
# path('focuse/',map.views.focuse,name='focuse'),
