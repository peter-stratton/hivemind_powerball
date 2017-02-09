# dashboard/views.py

from django.http import Http404, HttpResponse
from django.shortcuts import render

from ticket.forms import TicketForm
from ticket.utils import get_golden_ticket
from hive.models import Drone


def main_view(request):
    """Primary application view, '/' redirects here"""
    ticket = get_golden_ticket()
    drones = Drone.objects.all()
    drone_list = []
    for drone in drones:
        drone_list.append([drone.full_name,
                           ([x.value for x in drone.whiteball_set.all()],
                            [x.value for x in drone.redball_set.all()])])
    drone_field = {'headers': ['Drone Name', 'Drone Ticket'],
                   'rows': drone_list}
    form = TicketForm()
    return render(request,
                  'dashboard/main.html',
                  {'golden_ticket': ticket,
                   'drones': drone_field,
                   'form': form})
