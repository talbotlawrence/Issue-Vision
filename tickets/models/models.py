from django.contrib.auth.models import *
# from django.db.models import Avg
from django.db import models

#######################################################################################################

options_status = (          
        (0, 'Open'),
        (1, 'Closed'),
        (2, 'Hold'),
    )

options_priority = (          
        (0, 'Low'),
        (1, 'High'),
        (2, 'Nothing is working!'),
    )

#######################################################################################################

class Ticket(models.Model):
    status = models.IntegerField(default=0, choices=options_status)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    raised_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField(default=1, choices=options_priority)
    submitted = models.DateTimeField(auto_now_add=True)

#######################################################################################################

class Assign(models.Model):
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )

#######################################################################################################

class Image(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )
    image_path = models.ImageField(upload_to='images/', blank=True)

#######################################################################################################

class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True, null=True)
    submitted = models.DateTimeField(auto_now_add=True)

####################################################################################################