from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from tickets.models.models import Ticket

# PRIORITY_CHOICES = (
#     ('low', 'Low'),
#     ('high', 'High'),
#     ('catastrophe', 'Catastrophe'),
#     )

class TicketForm(forms.ModelForm):

    # PRIORITY_CHOICES = (
    # ('low', 'Low'),
    # ('high', 'High'),
    # ('catastrophe', 'Catastrophe'),
    # )

    class Meta:
        model = Ticket
        widgets = {
                    'priority': forms.TextInput(attrs={'class': 'form-control'}),
                    # 'raised_by_id': forms.CharField(initial=1),
                    # 'priority': forms.ChoiceField(attrs={'class': 'form-control'}),
                    'subject': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.TextInput(attrs={'class': 'form-control'})
                   
        }
        fields = ('priority', 'subject', 'description')