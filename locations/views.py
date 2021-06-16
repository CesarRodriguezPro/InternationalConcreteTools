from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Locations
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LocationsCreateView(LoginRequiredMixin, CreateView):
    model = Locations
    fields = '__all__'
    success_url = reverse_lazy('locations:listView')


class LocationUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Locations
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('locations:listView')


class LocationListView(LoginRequiredMixin, ListView):
    model = Locations
    paginate_by = 15
    template_name = "locations/listView.html"


class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Locations
    success_url = reverse_lazy('locations:listView')



