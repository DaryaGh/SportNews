from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(label='Username', widget=forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email' , 'autocomplete': 'off'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name' , 'autocomplete': 'off'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name' , 'autocomplete': 'off'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password-1' , 'autocomplete': 'off'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password-2' , 'autocomplete': 'off'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
        }