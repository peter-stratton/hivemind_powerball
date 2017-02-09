# ticket/views.py
import json

from django.shortcuts import render
from django.http import HttpResponse, Http404

from .forms import TicketForm
from hive.models import Drone
from .models import WhiteBall, RedBall
from .utils import get_golden_ticket


def new_ticket(request):
    if request.is_ajax() and request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            drone = Drone.objects.create(first_name=data['first_name'],
                                         last_name=data['last_name'])
            white_vals = [v for k, v in data.items() if 'white' in k.lower()]
            for val in white_vals:
                drone.whiteball_set.create(value=val)
            drone.redball_set.create(value=data['red1'])
            golden_ticket = get_golden_ticket()
            return HttpResponse(json.dumps({'drone_name': drone.full_name,
                                            'white_vals': white_vals,
                                            'red_val': data['red1'],
                                            'golden_ticket': golden_ticket}),
                                content_type="application/json")
        else:
            return HttpResponse(form.errors.as_json)
    else:
        raise Http404
