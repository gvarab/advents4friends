from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Calendar, Door


class CalendarList(ListView):
    model = Calendar


class CalendarDetail(DetailView):
    model = Calendar


class DoorDetail(DetailView):
    model = Door


class NewCalendar(CreateView):
    model = Calendar
    fields = ['name', ]

    def get_success_url(self):
        return reverse('calendar_list')


class EditCalendar(UpdateView):
    model = Calendar
    fields = ['name', ]

    def get_success_url(self):
        return reverse('calendar_list')


class NewDoor(CreateView):
    model = Door
    fields = ['number', 'content', ]
    calendar = None

    def dispatch(self, request, *args, **kwargs):
        calendar_pk = kwargs.get('cal')
        self.calendar = Calendar.objects.get(pk=calendar_pk)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.calendar.pk])

    def form_valid(self, form):
        form.instance.calendar = self.calendar
        return super().form_valid(form)