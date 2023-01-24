import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Import Django authentication user system
STATUS = ((0, 'Unapproved'), (1, 'Approved'))

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    created_date = models.DateTimeField(auto_now=True)
    booking_date = models.DateField(auto_now=False)
    booking_time =models.TimeField(auto_now=False)
    number_guests = models.IntegerField()
    booking_comments = models.TextField(max_length=500, blank=True)
    high_chair = models.BooleanField(null=False, blank=False, default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return self.title

class User_application(models.Model):
    user = models.TextField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=9)
    email = models.EmailField()
