from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from tickets.forms.forms import UserForm
from tickets.models.models import *
from django.contrib.auth.models import User


def index(request):
    template_name = 'index.html'
    # all_tickets = Ticket.objects.filter(quantity__gt=0).order_by('-id')[:20]
    all_tickets = Ticket.objects.all().order_by('-id')[:20]
    # tech_user = User.objects.get(username='talbotlawrence')
    # tech = Assign.objects.filter(id=0)
    # assigned_tech.id =     
    # print(assigned_tech)

    return render(request, template_name, {'tickets': all_tickets})


# Create your views here.
def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            # profile = Profile(user_id=user.id)
            # profile.save()

            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    return render(request, 'login.html', {}, context)       #study this line

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')

def list_tickets(request):
    # all_tickets = Ticket.objects.filter(quantity__gt=0)
    all_tickets = Ticket.objects.all()     
     
    template_name = 'ticket/list.html'
    return render(request, template_name, {'tickets': all_tickets})


# def profile(request):
    """This function allows the user to access his/her profile information.
    
    Arguments:
        request (List): A list of tuples from the database pertaining to payment
    
    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        payment (Dict): This is the payment information stored inside of a dictionary

    Author: Talbot Lawrence
       
    """
#     user = request.user
#     user_profile = Profile.objects.get(pk=user.id)
#     average_rating = user_profile.get_average_rating(user)
#     context = { 'profile': user_profile, 'average_rating': average_rating }
#     template_name = 'profile.html'
#     return render(request, template_name, context)


# def add_payment(request):
#     template_name = 'addpayment.html'
#     return render(request, template_name, {})