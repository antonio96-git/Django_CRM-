from django import forms
from django.contrib.auth.models import User                # importavamo model
from django.contrib.auth.forms import UserCreationForm
from .models import Record

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password1', 'password2')

    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(label='', max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Record
        fields  = ('first_name','last_name', 'email', 'phone', 'address', 'country', 'city')

    first_name = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
    }))
    email = forms.EmailField(label='', required=True, max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    phone = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone',
    }))
    address = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Address',
    }))
    country = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Country',
    }))
    city = forms.CharField(label='', required=True, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'City',
    }))