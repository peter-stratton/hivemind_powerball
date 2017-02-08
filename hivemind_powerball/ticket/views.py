# ticket/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TicketForm
from hive.models import Drone
from .models import WhiteBall, RedBall


def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            drone = Drone.objects.create(first_name=data['first_name'],
                                         last_name=data['last_name'])
            white_vals = [v for k, v in data.items() if 'white' in k.lower()]
            for val in white_vals:
                drone.whiteball_set.create(value=val)
            drone.redball_set.create(value=data['red1'])
            return HttpResponseRedirect('/hive/drones/')
    else:
        form = TicketForm()

    return render(request, 'ticket/ticket_form.html', {'form': form})
