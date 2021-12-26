from django.forms import ModelForm
from order.models import Order
from django import forms


class OrderForm(ModelForm):
        class Meta:
            model = Order
            fields = ( 'order_code', 'payment_code')
            order_code = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input'})),
            payment_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input'})),
            