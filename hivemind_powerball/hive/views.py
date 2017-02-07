from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .models import Drone


# edit views
class DroneCreate(CreateView):
    model = Drone
    fields = ['first_name', 'last_name']


class DroneUpdate(UpdateView):
    model = Drone
    fields = ['first_name', 'last_name']


class DroneDelete(DeleteView):
    model = Drone
    success_url = reverse_lazy('hive:drone-list')


# examination views
class DroneDetail(DetailView):
    model = Drone


class DroneList(ListView):
    model = Drone
    context_object_name = 'drone_list'

