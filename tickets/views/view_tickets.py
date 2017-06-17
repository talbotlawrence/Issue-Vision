# from django.shortcuts import render
# from tickets.models.models import Ticket

# def list_category_tickets(request, category_id):
    """
    Display all of the tickets for a given category.

    Arguments:
        request (GET): Get data from ticket table,
        category_id(foreign key): The Id of the selected category.

    Returns: render, Combines template_name with the given dictionary and passes HttpResponse object with that rendered text.

    Author: Talbot Lawrence
    """

    # all_tickets_in_cat = Ticket.objects.filter(category_id=category_id, is_active=1, quantity__gt=0)
    # category_name = all_tickets_in_cat[0].category
    # print(category_name)
    # template_name = 'categorytickets.html'
    # return render(request, template_name, {'tickets': all_tickets_in_cat, 'name': category_name})