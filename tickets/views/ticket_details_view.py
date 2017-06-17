from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from tickets.forms.forms import UserForm
# from tickets.forms.form_ticket import TicketForm
from tickets.models.models import *


def ticket_details(request, ticket_id):
    """This function allows the ticket's information to be displayed as prescribed.

    Author: Talbot Lawrence
        
    Args:
        request (List): A list of tuples from the database

    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        ticket (Dict): This is the ticket's information stored inside of a dictionary
    """
    template_name = 'ticket/ticket_details.html'
    chosen_ticket = Ticket.objects.get(pk=ticket_id)

    return render(request, template_name, {'ticket': chosen_ticket})