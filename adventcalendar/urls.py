from django.urls import path
from adventcalendar.views import CalendarList, CalendarDetail, DoorDetail, NewCalendar, EditCalendar, NewDoor

urlpatterns = [
    path('', CalendarList.as_view(), name='calendar_list'),
    path('<int:pk>/', CalendarDetail.as_view(), name='calendar_detail'),
    path('<int:cal>/<int:pk>/', DoorDetail.as_view(), name='door_detail'),
    path('new_calendar/', NewCalendar.as_view(), name='calendar_new'),
    path('<int:pk>/edit/', EditCalendar.as_view(), name='calendar_edit'),
    path('<int:cal>/new_door/', NewDoor.as_view(), name='door_new'),
]