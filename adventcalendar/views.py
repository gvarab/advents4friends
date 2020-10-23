from django.views.generic import ListView
from django.views.generic import DetailView
from adventcalendar.models import Calendar


class CalendarList(ListView):

    model = Calendar


class CalendarDetail(DetailView):

    model = Calendar
