from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Calendar, Door, Snippet
from .forms import DoorForm


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

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(creator=self.request.user)
        else:
            return Calendar.objects.none()


class CalendarDetail(DetailView):
    model = Calendar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object().theme
        doors_open = self.request.GET.get('doorsOpen', None)
        sorted_doors = self.get_object().door_set.all().order_by('position')
        openable_doors = []
        for door in list(sorted_doors):
            if door.is_openable and not door.open:
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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        door = self.get_object()
        if request.user != door.calendar.creator:
            if not door.is_openable:
                return redirect('calendar_detail', door.calendar.slug)
            door.open = True
            door.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme = self.get_object().calendar.theme
        previous_door = self.get_object().calendar.get_previous_door(self.get_object())
        next_door = self.get_object().calendar.get_next_door(self.get_object())
        print(previous_door)
        print(next_door)
        context['calendar_style'] = STYLES[theme]
        context['previous_door'] = previous_door
        context['next_door'] = next_door
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


class EditCalendar(PermissionRequiredMixin, UpdateView):
    model = Calendar
    fields = ['name', 'theme']

    def get_success_url(self):
        return reverse('calendar_detail', args=[self.object.slug])

    def has_permission(self):
        return self.request.user == self.get_object().creator


class CopyCalendar(PermissionRequiredMixin, CreateView):
    model = Calendar
    fields = ['name']
    template_name = 'adventcalendar/calendar_copy_form.html'
    original_calendar = None

    def get_success_url(self):
        return reverse('calendar_list')

    def has_permission(self):
        self.original_calendar = Calendar.objects.get(slug=self.kwargs.get('slug'))
        return self.request.user == self.get_object().creator

    def form_valid(self, form):

        form.instance.creator = self.request.user
        form.instance.number_of_doors = self.original_calendar.number_of_doors
        form.instance.start_date = self.original_calendar.start_date
        form.instance.theme = self.original_calendar.theme
        response = super().form_valid(form)
        form.instance.copy_doors(self.original_calendar)
        return response


class DeleteCalendar(PermissionRequiredMixin, DeleteView):
    model = Calendar

    def get_success_url(self):
        return reverse('calendar_list')

    def has_permission(self):
        return self.request.user == self.get_object().creator


class EditDoor(PermissionRequiredMixin, UpdateView):
    model = Door
    form_class = DoorForm

    def get_success_url(self):
        return reverse('door_detail', args=[self.object.slug])

    def has_permission(self):
        return self.request.user == self.get_object().calendar.creator


class ContactPrivacy(TemplateView):
    template_name = 'adventcalendar/contact_privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['privacy_snippet'] = Snippet.objects.get(name='privacy').content
        context['contact_snippet'] = Snippet.objects.get(name='contact').content
        return context
