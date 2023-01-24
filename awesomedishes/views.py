from django.shortcuts import render

# Create your views here.

def open_home_page(request):
    return render(request, 'restaurant_booking/home_page.html')