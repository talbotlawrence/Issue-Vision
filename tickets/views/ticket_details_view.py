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
	chosen_ticket = ticket.objects.get(pk=ticket_id)

	if 'opinion' in request.POST:
		try:
			opinion = Opinion.objects.get(user=request.user, ticket=chosen_ticket)

		except Opinion.DoesNotExist:
			opinion = Opinion(
				ticket=chosen_ticket,
				user=request.user
			)

		if request.POST['opinion'] == 'like':
			opinion.like = 1
		else:
			opinion.like = 0

		opinion.save()

	if 'ticket.id' in request.POST:

		try:
			order = Order.objects.get(user=request.user, payment=None)

		except Order.DoesNotExist:
			order = Order(
				user = request.user,
				payment = None
				)
			order.save()

		try:
			pos = ticketOrder.objects.filter(order=order, ticket=chosen_ticket).count()
			if chosen_ticket.quantity > pos:
				po = ticketOrder(
				order = order,
				ticket = chosen_ticket
				)
				po.save()

		except ticketOrder.DoesNotExist:
			po = ticketOrder(
				order = order,
				ticket = chosen_ticket
				)
			po.save()

	elif request.method == 'GET':
		chosen_ticket = ticket.objects.get(pk=ticket_id)
		template_name = 'ticket/ticket_details.html'
	return render(request, template_name, {'ticket': chosen_ticket})