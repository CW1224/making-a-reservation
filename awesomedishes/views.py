from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm

# Create your views here.

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('created_date')
    template_name = 'index.html'

def open_home_page(request):
    return render(request, 'restaurant_booking/index.html')

def make_a_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('open_home_page')
    
    form = BookingForm()
    context = {
        'form' : form
    }

    return render(request, 'restaurant_booking/make_a_reservation.html', context)