from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from tickets.models.models import Ticket

class TicketForm(forms.ModelForm):

	class Meta:
		model = Ticket
		widgets = {
		            'priority': forms.TextInput(attrs={'class': 'form-control'}),
		            'subject': forms.TextInput(attrs={'class': 'form-control'}),
		            'description': forms.TextInput(attrs={'class': 'form-control'})
		            # 'price': forms.NumberInput(attrs={'class': 'form-control'}),
		            # 'quantity': forms.NumberInput(attrs={'class': 'form-control'})

		}
		fields = ('status', 'subject', 'description', 'raised_by','priority')