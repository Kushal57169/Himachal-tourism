# tours/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('package/<int:pk>/book/', views.book_package_view, name='book_package'),
    path('chat/', views.smart_chat_view, name='smart_chat'),
    path('taxi/', views.taxi_booking_view, name='taxi_booking'),
    path('ticket/<int:booking_id>/download/', views.download_ticket, name='download_ticket'),
    path('packages/', views.all_packages_view, name='all_packages'),
    path('booking/<int:id>/reschedule/', views.reschedule_booking, name='reschedule_booking'),
    path('booking/<int:id>/cancel/', views.cancel_booking, name='cancel_booking'),

    path('taxi/<int:id>/reschedule/', views.reschedule_taxi, name='reschedule_taxi'),
    path('taxi/<int:id>/cancel/', views.cancel_taxi, name='cancel_taxi'),
    path('taxi/', views.taxi_booking_view, name='taxi'),





]



