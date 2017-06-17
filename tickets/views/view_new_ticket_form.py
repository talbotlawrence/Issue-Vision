from django.shortcuts import render
# from django.template import RequestContext
from tickets.forms.form_ticket import TicketForm
from tickets.models.models import *
from django.utils.datastructures import MultiValueDictKeyError 
def new_ticket(request):
    """This function allows the user to add a ticket to the Ticket table to be sold.

    Arguments:
        request: django request format containing information about the request.

    Returns:
        request: django request format containing information about the request.
        template_name (HTML): The webpage's structure
        ticket_form (Dict): This is the form information formating a ticket information

    Author: Talbot Lawrence
    """
    if request.method == 'GET':
        template_name = 'ticket_create.html'
        ticket_form = TicketForm()
        print("My ticket form is {}".format(ticket_form))
        return render(request, template_name, {'ticket_form': ticket_form})

    elif request.method == 'POST':
        form_data = request.POST
        error_message = None
       
        if error_message is not None:
            ticket_form = TicketForm(request.POST, request.FILES)
            print("My ticket form is {}".format(ticket_form))
            template_name = 'ticket_create.html'
            return render(request, template_name, { 'ticket_form': ticket_form, 'error_message': error_message })
  
        t = Ticket(
            # seller = request.user,
            priority = form_data['priority'],
            subject = form_data['subject'],
            description = form_data['description']
            
            # category = Category.objects.get(pk=form_data['category']),
            # image_path = image_path,
            # local_delivery = delivery,
            # city = city,
            # is_active = 1
        )
            
        t.save()
        template_name = 'ticket_details.html'
        return render(request, template_name, { 'ticket': t })