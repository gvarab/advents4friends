from django.urls import include, path
from adventcalendar.views import CalendarList, CalendarDetail, DoorDetail, NewCalendar,\
    EditCalendar, EditDoor, DeleteCalendar

urlpatterns = [
    path('', CalendarList.as_view(), name='calendar_list'),
    path('new_calendar/', NewCalendar.as_view(), name='calendar_new'),
    path('calendar/<slug:slug>/', CalendarDetail.as_view(), name='calendar_detail'),
    path('calendar/<slug:slug>/edit/', EditCalendar.as_view(), name='calendar_edit'),
    path('calendar/<slug:slug>/delete/', DeleteCalendar.as_view(), name='calendar_delete'),
    path('door/<slug:slug>/', DoorDetail.as_view(), name='door_detail'),
    path('door/<slug:slug>/edit/', EditDoor.as_view(), name='door_edit'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]