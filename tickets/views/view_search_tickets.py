import operator
from django.shortcuts import render
from django.db.models import Q
from django.template import RequestContext
from tickets.models.models import Ticket



def search_tickets(request):
    
    form_data = request.GET
    iterable_form_data = form_data.dict()
    
    search_box = iterable_form_data['Search']
    tickets = Ticket.objects.filter(Q(description__icontains=search_box) | Q(subject__icontains=search_box) | Q(status__icontains=search_box) | Q(priority__icontains=search_box))
    template_name = 'search_tickets.html'

    return render(request, template_name, {'tickets': tickets})