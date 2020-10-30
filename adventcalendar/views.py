from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
        form.instance.initialize_doors()
        return response


class EditCalendar(UpdateView):
    model = Calendar
    fields = ['name', ]

    def get_success_url(self):
        return reverse('calendar_list')


class DeleteCalendar(DeleteView):
    model = Calendar

    def get_success_url(self):
        return reverse('calendar_list')


class EditDoor(UpdateView):
    model = Door
    fields = ['content', ]

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.object.calendar.pk])