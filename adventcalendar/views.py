from datetime import timedelta
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Calendar, Door


STYLES = {
    Calendar.Theme.PLAIN: 'calendar-plain',
    Calendar.Theme.RED: 'calendar-red',
    Calendar.Theme.CUPCAKE: 'calendar-cupcakes',
    Calendar.Theme.TREE: 'calendar-trees',
    Calendar.Theme.TWIGS: 'calendar-twigs',
    Calendar.Theme.SNOWMEN: 'calendar-snowmen',
}

IMAGE_CREDITS = {
    Calendar.Theme.PLAIN: None,
    Calendar.Theme.RED: 'https://www.flickr.com/photos/bmiphone/23025603455/',
    Calendar.Theme.CUPCAKE: 'https://www.flickr.com/photos/bmiphone/23025603455/',
    Calendar.Theme.TREE: 'https://www.flickr.com/photos/bmiphone/23025603455/',
    Calendar.Theme.TWIGS: 'https://www.flickr.com/photos/bmiphone/23025603455/',
    Calendar.Theme.SNOWMEN: 'https://www.flickr.com/photos/bmiphone/23025603455/',
}


class CalendarList(ListView):
    model = Calendar


class CalendarDetail(DetailView):
    model = Calendar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object().theme
        doors_open = self.request.GET.get('doorsOpen', None)
        sorted_doors = self.get_object().door_set.all().order_by('position')
        openable_doors = []
        for door in list(sorted_doors):
            if door.is_openable:
                 openable_doors.append(door)
        context.update({
            'calendar_style': STYLES[theme],
            'credits': IMAGE_CREDITS[theme],
            'doors_open': doors_open,
            'sorted_doors': sorted_doors,
            'openable_doors': openable_doors,
            'number_of_openable_doors': len(openable_doors),
        })
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
        form.instance.creator = self.request.user
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