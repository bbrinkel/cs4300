from django import forms

class BookingForm(forms.Form):
    user = forms.CharField(max_length=50)
    seat_number = forms.CharField(max_length=2)

class HistoryForm(forms.Form):
    user = forms.CharField(max_length=50)