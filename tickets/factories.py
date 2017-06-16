"""
bangazon factory to create sample data to seed a database using Faker 
"""

import factory
from tickets.models.models import *
from django.contrib.auth.models import *

#######################################################################################################

class UserFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the user table in the database.

    ----Fields----
    username('word'): fake name of a username
    first_name('first_name'): fake first name
    last_name('last_name'): fake last name
    password('word'): fake password
    email('email'): fake email
    last_login('date'): fake date
    is_supervisor: 0
    is_active: 0
    is_staff: 0
    date_joined('date'): fake date

    Author: Talbot Lawrence
    """

    class Meta:
        model = User
    username = factory.Faker('name_male')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    last_login = factory.Faker('date')
    is_superuser = 0
    is_active = 0
    is_staff = 0
    date_joined = factory.Faker('date')

#######################################################################################################

class TicketFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the ticket table in the database.

    ----Fields----
    status: Open
    subject('bs'): fake title for ticket
    description('bs'): fake description of a ticket
    raised_by(Iterator[User]): iterates over user.objects.all
    priority: High
    submitted('date'): fake date

   
    Author: Talbot Lawrence
    """
    class Meta:
        model = Ticket
    status = "Open"
    subject = factory.Faker('bs')
    description = factory.Faker('bs')
    raised_by = factory.Iterator(User.objects.all())
    priority = "High"
    submitted = factory.Faker('date')

#######################################################################################################

class AssignFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Assign
    assignee = factory.Iterator(User.objects.all())
    ticket = factory.Iterator(Ticket.objects.all())

#######################################################################################################

class ImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Image
    user = factory.Iterator(User.objects.all())
    ticket = factory.Iterator(Ticket.objects.all())
    image_path = factory.Faker('file_path', depth=1, category=None, extension=None)

#######################################################################################################

class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment
    user = factory.Iterator(User.objects.all())
    ticket = factory.Iterator(Ticket.objects.all())
    description = factory.Faker('bs')
    submitted = factory.Faker('date')