# ticket/views.py
"""Ticket app views"""

import json

from django.http import HttpResponse, Http404

from .forms import TicketForm
from hive.models import Drone
from .utils import get_golden_ticket


def new_ticket(request):
    """
    Responds to AJAX Post requests to generate a new `Drone` and associated
    powerball ticket.  Part of the expected response is the updated
    `golden_ticket`, so we query for that as well.
    """
    if request.is_ajax() and request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            drone = Drone.objects.create(first_name=data['first_name'],
                                         last_name=data['last_name'])
            # iterate over the form data and collect the 5 white ball fields
            white_vals = [v for k, v in data.items() if 'white' in k.lower()]
            for val in white_vals:
                drone.whiteball_set.create(value=val)
            drone.redball_set.create(value=data['red1'])
            golden_ticket = get_golden_ticket()
            return HttpResponse(json.dumps({'drone_name': drone.full_name,
                                            'white_vals': white_vals,
                                            'red_val': data['red1'],
                                            'golden_ticket': golden_ticket,
                                            'status': 'success'}),
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({'status': 'failure',
                                            'error_list':
                                            form.errors['__all__']}),
                                content_type="application/json")
    else:
        raise Http404
