"""
bangazon custom command to build database
"""

import os
from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import makemigrations
from tickets.factories import *                           #uncomment this line when SQL is working!!

class Command(BaseCommand):
    """
    Defines the command 'builddb', which is a shortcut for running
    the necessary shell commands to generate our database's tables and
    load our data to them via Faker. These commands are, in order:
    1. python manage.py makemigrations tickets
    2. python manage.py migrate
    3. (Factory Calls): Ticket, Image, and Comment

    Author: Talbot Lawrence
    """

    def handle(self, *args, **options):
        os.system('rm tickets/migrations/*.py;')   #deletes all of the .py files in the migrations directory.
        os.system('touch tickets/migrations/__init__.py;') #re-create the __init__.py file.
        os.system('rm db.sqlite3;')  #deletes the database file.    