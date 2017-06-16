"""
bangazon custom command to build database
"""

from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from tickets.factories import *

class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    the necessary shell commands to generate our database's tables and
    load our data to them via Faker. These commands are, in order:
    1. python manage.py makemigrations api
    2. python manage.py migrate
    3. (Factory Calls): Ticket, Image, and Comment


    Author: Talbot Lawrence
    """

    def handle(self, *args, **options):
        management.call_command('makemigrations')       #study this line
        management.call_command('migrate')              #study this line
        UserFactory.create_batch(size=10) 
        TicketFactory.create_batch(size=20)             #what determines the size?
        AssignFactory.create_batch(size=20)
        ImageFactory.create_batch(size=5)
        CommentFactory.create_batch(size=5)