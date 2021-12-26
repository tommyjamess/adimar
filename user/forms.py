from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import BillingInfo
from django.forms import ModelForm
from order.models import OrderPlaced


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter last_name'}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'password'}))

    password1 = forms.CharField(
        label="Password"
    )
    password2 = forms.CharField(
        label= "Repeat Password"
    )


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class BillingForm(ModelForm):
        class Meta:
            model = BillingInfo
            fields = ( 'first_name', 'last_name', 'street', 'nearest_stop', 'city', 'state', 'phone_one', 'phone_two', )
            first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input'})),
            last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input'})),
            street = forms.CharField(required=True, widget=forms.TextInput()),
            nearest_stop = forms.CharField(required=True, widget=forms.TextInput()),
            city = forms.CharField(required=True, widget=forms.TextInput()),
            state = forms.CharField(required=True, widget=forms.TextInput()),
            phone_one = forms.CharField(required=True, widget=forms.TextInput()),
            phone_two = forms.CharField(required=True, widget=forms.TextInput()),



