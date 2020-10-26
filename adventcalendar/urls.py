from django.urls import path
from adventcalendar.views import CalendarList
from adventcalendar.views import CalendarDetail
from adventcalendar.views import DoorDetail

urlpatterns = [
    path('', CalendarList.as_view(), name='calendar_list'),
    path('<int:pk>/', CalendarDetail.as_view(), name='calendar_detail'),
    path('<int:cal>/<int:pk>/', DoorDetail.as_view(), name='door_detail'),
]