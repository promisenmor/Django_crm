from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class signUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}

    def __init__(self, *args: Any, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].label = ''

# creating Add Record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class':'form-control'}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class':'form-control'}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone', 'class':'form-control'}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class':'form-control'}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class':'form-control'}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class':'form-control'}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class':'form-control'}), label="")

    class Meta:
        model = Record
        exclude = ("user",)