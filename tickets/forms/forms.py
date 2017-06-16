from django.contrib.auth.models import User
# from tickets.models.models import Profile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.TextInput(attrs={'class': 'form-control'}),
                    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control'})
                }
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control'})
                }
        fields = ('first_name', 'last_name')


#do I need this below???  I don't think so!!!
# class ProfileForm(forms.ModelForm):
#     phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), validators=[validate_phone])
#     zipcode = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}), validators=[validate_zip])

#     class Meta:
#         model = Profile
#         widgets = {
#                     'address': forms.TextInput(attrs={'class': 'form-control'}),
#                     'city': forms.TextInput(attrs={'class': 'form-control'}),
#                     'state': forms.TextInput(attrs={'class': 'form-control'})
#                 }
#         fields = ('address', 'city', 'state', 'zipcode', 'phone_number')