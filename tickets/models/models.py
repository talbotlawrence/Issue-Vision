from django.contrib.auth.models import *
from django.db import models

#######################################################################################################

PRIORITY_CHOICES = (
    ('low', 'Low'),
    ('high', 'High'),
    ('catastrophe', 'Catastrophe'),
    )

#######################################################################################################

class Ticket(models.Model):
    status = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    raised_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES)
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