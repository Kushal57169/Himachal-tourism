from django.db import models
from django.contrib.auth.models import User

class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    image = models.ImageField(upload_to='packages/images/')
    video = models.FileField(upload_to='packages/videos/', blank=True, null=True)  # Optional video

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    travel_date = models.DateField()
    members = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    coupon_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_name} - {self.package.title}"

class TaxiBooking(models.Model):
    VEHICLE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('7-Seater', '7-Seater'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    travel_date = models.DateField()
    members = models.PositiveIntegerField()
    estimated_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type} to {self.destination}"
