# tours/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'travel_date', 'members']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }
# tours/forms.py
from django import forms
from .models import TaxiBooking

class TaxiBookingForm(forms.ModelForm):
    class Meta:
        model = TaxiBooking
        fields = ['pickup_point', 'destination', 'vehicle_type', 'travel_date', 'members']
        widgets = {
            'pickup_point': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pickup location'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'members': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of members'}),
        }
