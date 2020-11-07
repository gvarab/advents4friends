from django.urls import path
from adventcalendar.views import CalendarList, CalendarDetail, DoorDetail, NewCalendar,\
    EditCalendar, EditDoor, DeleteCalendar

urlpatterns = [
    path('', CalendarList.as_view(), name='calendar_list'),
    path('new_calendar/', NewCalendar.as_view(), name='calendar_new'),
    path('calendar/<int:pk>/', CalendarDetail.as_view(), name='calendar_detail'),
    path('calendar/<int:pk>/edit/', EditCalendar.as_view(), name='calendar_edit'),
    path('calendar/<int:pk>/delete/', DeleteCalendar.as_view(), name='calendar_delete'),
    path('door/<int:pk>/', DoorDetail.as_view(), name='door_detail'),
    path('door/<int:pk>/edit/', EditDoor.as_view(), name='door_edit'),
]