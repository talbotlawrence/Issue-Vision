from django.contrib.auth.models import *
# from django.db.models import Avg
from django.db import models

#######################################################################################################

class Ticket(models.Model):
    # status = models.IntegerField(default=0, choices=options_status)
    status = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    raised_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # priority = models.IntegerField(default=1, choices=options_priority)
    priority = models.CharField(max_length=25)
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