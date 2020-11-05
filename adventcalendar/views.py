from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Calendar, Door


STYLES = {
    Calendar.Theme.PLAIN: 'calendar-plain',
    Calendar.Theme.CUPCAKE: 'calendar-cupcakes',
    Calendar.Theme.TREE: 'calendar-trees',
    Calendar.Theme.HARE: 'calendar-hare',
}


class CalendarList(ListView):
    model = Calendar


class CalendarDetail(DetailView):
    model = Calendar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object().theme
        context['calendar_style'] = STYLES[theme]
        return context


class DoorDetail(DetailView):
    model = Door

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object().calendar.theme
        context['calendar_style'] = STYLES[theme]
        return context


class NewCalendar(CreateView):
    model = Calendar
    fields = ['name', 'number_of_doors', 'start_date', 'theme']

    def get_success_url(self):
        return reverse('calendar_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.initialize_doors()
        return response


class EditCalendar(UpdateView):
    model = Calendar
    fields = ['name', 'theme']

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.object.pk])


class DeleteCalendar(DeleteView):
    model = Calendar

    def get_success_url(self):
        return reverse('calendar_list')


class EditDoor(UpdateView):
    model = Door
    fields = ['content', ]

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.object.calendar.pk])