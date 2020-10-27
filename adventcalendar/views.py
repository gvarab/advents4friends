from django.urls import reverse
from django.utils import timezone
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
    fields = ['name', 'number_of_doors', ]

    def get_success_url(self):
        return reverse('calendar_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        for i in range(1, form.instance.number_of_doors+1):
            Door.objects.create(number=i, content="", opening_date=timezone.now(), calendar=form.instance)
        return response


class EditCalendar(UpdateView):
    model = Calendar
    fields = ['name', ]

    def get_success_url(self):
        return reverse('calendar_list')


class EditDoor(UpdateView):
    model = Door
    fields = ['content', ]

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.object.calendar.pk])