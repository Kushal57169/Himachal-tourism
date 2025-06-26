# tours/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Form is invalid')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    bookings = Booking.objects.filter(user=request.user)
    taxis = TaxiBooking.objects.filter(user=request.user)  # renamed
    return render(request, 'profile.html', {
        'bookings': bookings,
        'taxis': taxis  # match template
    })



def home_view(request):
    all_packages = TourPackage.objects.all()
    price_filter = request.GET.get('price')

    if price_filter == 'low':
        all_packages = all_packages.filter(price__lt=10000)
    elif price_filter == 'medium':
        all_packages = all_packages.filter(price__range=(10000, 20000))
    elif price_filter == 'high':
        all_packages = all_packages.filter(price__gt=20000)

    top_packages = TourPackage.objects.all()[:5]  # First 5 for carousel
    return render(request, 'home.html', {
        'top_packages': top_packages,
        'all_packages': all_packages,
    })

from .forms import BookingForm
from .models import TourPackage, Booking
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@login_required
def book_package_view(request, pk):
    package = TourPackage.objects.get(id=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.coupon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            booking.save()

            # 📩 Email content
            context = {
                'username': booking.full_name,
                'package': package,
                'travel_date': booking.travel_date,
                'members': booking.members,
                'coupon': booking.coupon_code,
            }

            subject = "🎫 Your Himachal Tour Booking Confirmation"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [booking.email]

            text_content = f"Hi {booking.full_name}, your booking to {package.title} is confirmed!"
            html_content = render_to_string("emails/booking_email.html", context)

            email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect('profile')  # Show in profile
    else:
        form = BookingForm()

    return render(request, 'book_package.html', {'form': form, 'package': package})

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def smart_chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        prompt = f"""
You are a helpful Himachal tour planner.
Suggest 2-3 packages for someone with this message:
"{user_message}"

Give suggestions like:
🏞️ <Title>
💰 ₹<Price> | <Days> Days
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=300
            )
            reply = response.choices[0].message["content"]
        except Exception as e:
            reply = f"⚠️ Error: {str(e)}"

        return JsonResponse({'reply': reply})
    
    return render(request, 'chat.html')

from .models import TaxiBooking
from .forms import TaxiBookingForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

@login_required
def taxi_booking_view(request):
    if request.method == 'POST':
        form = TaxiBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Basic price logic (customize as needed)
            base_price = 2000
            if booking.vehicle_type == 'SUV':
                base_price += 1000
            elif booking.vehicle_type == '7-Seater':
                base_price += 1500

            booking.estimated_price = base_price
            booking.save()

            # ✉️ Send confirmation email
            send_mail(
                subject="Taxi Booking Confirmed",
                message=(
                    f"Hi {request.user.username},\n\n"
                    f"Your taxi to {booking.destination} is confirmed!\n"
                    f"Pickup: {booking.pickup_point}\n"
                    f"Date: {booking.travel_date}\n"
                    f"Vehicle: {booking.vehicle_type}\n"
                    f"Estimated Price: ₹{booking.estimated_price}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True
            )

            return redirect('profile')
    else:
        form = TaxiBookingForm()

    return render(request, 'taxi_booking.html', {'form': form})

from reportlab.pdfgen import canvas
from django.http import HttpResponse
@login_required
def download_ticket(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=ticket_{booking_id}.pdf'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 18)
    p.drawString(200, 800, "Himachal Tourism Ticket")

    p.setFont("Helvetica", 12)
    p.drawString(50, 750, f"Name: {booking.full_name}")
    p.drawString(50, 730, f"Email: {booking.email}")
    p.drawString(50, 710, f"Package: {booking.package.title}")
    p.drawString(50, 690, f"Members: {booking.members}")
    p.drawString(50, 670, f"Travel Date: {booking.travel_date}")
    p.drawString(50, 650, f"Coupon Code: {booking.coupon_code}")

    p.drawString(50, 620, "Thank you for booking with Himachal Tourism!")

    p.showPage()
    p.save()
    return response

from .models import TourPackage
def all_packages_view(request):
    packages = TourPackage.objects.all()
    return render(request, 'all_packages.html', {'packages': packages})


from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, TaxiBooking

def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)
    booking.delete()
    messages.success(request, "Tour booking cancelled.")
    return redirect('profile')

def reschedule_booking(request, id):
    messages.info(request, "Rescheduling feature coming soon!")
    return redirect('profile')

def cancel_taxi(request, id):
    taxi = get_object_or_404(TaxiBooking, id=id, user=request.user)
    taxi.delete()
    messages.success(request, "Taxi booking cancelled.")
    return redirect('profile')

def reschedule_taxi(request, id):
    messages.info(request, "Rescheduling feature coming soon!")
    return redirect('profile')
