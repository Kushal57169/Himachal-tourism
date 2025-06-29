# Generated by Django 5.2.1 on 2025-06-22 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_booking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_point', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('7-Seater', '7-Seater')], max_length=20)),
                ('travel_date', models.DateField()),
                ('members', models.PositiveIntegerField()),
                ('estimated_price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
