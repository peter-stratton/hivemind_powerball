import json
from django.http import Http404, HttpResponse
from django.shortcuts import render

from ticket.forms import TicketForm
from hive.models import Drone
from ticket.models import WhiteBall, RedBall

# Create your views here.
def get_composite_ticket(request):
    if request.is_ajax():
        data = {'message': 'golden ticket'}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

def main_view(request):
    golden_ticket = ([1, 2, 3, 4, 5], 6)
    drones = Drone.objects.all()
    drone_list = []
    for drone in drones:
        drone_list.append([drone.full_name,
                           [x.value for x in drone.whiteball_set.all()],
                           [x.value for x in drone.redball_set.all()][0]])
    drone_field = {'headers': ['Drone Name', 'Whiteballs', 'Powerball'],
                   'rows': drone_list}
    form = TicketForm()
    return render(request,
                  'dashboard/main.html',
                  {'golden_ticket':golden_ticket,
                   'drones': drone_field,
                   'form': form})
