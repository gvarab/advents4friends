from django.urls import path
from adventcalendar.views import CalendarDetail
from adventcalendar.views import CalendarList

urlpatterns = [
    path('', CalendarList.as_view(), name='calendar_list'),
    path('<int:pk>/', CalendarDetail.as_view(), name='calendar_detail'),
]