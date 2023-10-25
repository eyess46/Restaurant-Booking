from django import forms
from .models import Order
from datetime import datetime





class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=1000)
    phone_number = forms.CharField(max_length=100)
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    time = forms.CharField(max_length=10000)
    number_of_people = forms.IntegerField()
    message = forms.CharField(max_length=10000)
    

    class Meta:
        model = Order
        fields =['name', 'phone_number', 'date_needed', 'email', 'time', 'number_of_people', 'message']