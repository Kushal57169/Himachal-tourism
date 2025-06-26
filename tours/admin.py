# tours/admin.py

from django.contrib import admin
from .models import TourPackage

admin.site.register(TourPackage)


from .models import TaxiBooking
admin.site.register(TaxiBooking)
