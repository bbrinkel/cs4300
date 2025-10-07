# Needed to import form
from django import forms

class BookingForm(forms.Form):
    """Form for validating User input in Seat page view"""
    user = forms.CharField(max_length=50)
    seat_number = forms.CharField(max_length=2)

class HistoryForm(forms.Form):
    """Form for validating User input in Booking page view"""
    user = forms.CharField(max_length=50)