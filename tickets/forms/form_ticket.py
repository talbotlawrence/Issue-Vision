from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from tickets.models.models import *

PRIORITY_CHOICES = (
('low', 'Low'),
('high', 'High'),
('catastrophe', 'Catastrophe'),
)

class TicketForm(forms.ModelForm):

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=True )


    class Meta:
        model = Ticket
        widgets = {
                    # 'raised_by_id': forms.CharField(initial=1),
                    # 'priority': forms.TextInput(attrs={'class': 'form-control'}),
                    # 'priority': forms.ChoiceField(attrs={'class': 'form-control'}),
                    'subject': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.TextInput(attrs={'class': 'form-control'})
                   
        }
        fields = ('priority', 'subject', 'description')