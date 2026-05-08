from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import MenuItem, Booking
from .forms import RegisterForm, BookingForm, ContactForm


def HomeView(request):
    featured = MenuItem.objects.filter(is_available=True)[:6]
    return render(request, 'restaurant/home.html', {'featured': featured})


def AboutView(request):
    return render(request, 'restaurant/about.html')


def MenuView(request):
    starters = MenuItem.objects.filter(category='starter', is_available=True)
    mains    = MenuItem.objects.filter(category='main',    is_available=True)
    desserts = MenuItem.objects.filter(category='dessert', is_available=True)
    drinks   = MenuItem.objects.filter(category='drink',   is_available=True)
    return render(request, 'restaurant/menu.html', {
        'starters': starters,
        'mains':    mains,
        'desserts': desserts,
        'drinks':   drinks,
    })


@login_required
def BookTableView(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, '🎉 Table booked successfully!')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'restaurant/book_table.html', {'form': form})


@login_required
def MyBookingsView(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'restaurant/my_bookings.html', {'bookings': bookings})


@login_required
def CancelBookingView(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'Booking cancelled.')
    return redirect('my_bookings')


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Message sent!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'restaurant/contact.html', {'form': form})


def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'restaurant/register.html', {'form': form})


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'restaurant/login.html', {'form': form})


def LogoutView(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')