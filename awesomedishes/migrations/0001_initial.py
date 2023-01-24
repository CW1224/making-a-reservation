# Generated by Django 3.2.16 on 2023-01-24 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('number_guests', models.IntegerField()),
                ('booking_comments', models.TextField(blank=True, max_length=500)),
                ('high_chair', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Unapproved'), (1, 'Approved')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-booking_date'],
            },
        ),
    ]
