from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'booking_time', 'booking_date', 'number_guests', 'high_chair', 'booking_comments']