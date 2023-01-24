from django.contrib import admin
from .models import Booking, User_application

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_date')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)

