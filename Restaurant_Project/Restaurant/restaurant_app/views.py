from django.shortcuts import render
from .models import MenuItem
from django.contrib.auth.decorators import login_required 

# Create your views here.
def HomeView(request):
    featured=MenuItem.objects.filter(is_available=True)[:6]
    return render(request, 'home.html', {'featured': featured})

def AboutView(request):
    return render(request, 'about.html')

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
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.user=request.user
            booking.save()
            messages.success(request, 'Table booked Successfully')
            return redirect ('my_bookings')
    else:
        form=BookingForm()
    return render(request,'restaurant/book_table.html', {'form':form})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'restaurant/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, 'Booking cancelled.')
    return redirect('my_bookings')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Message sent! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'restaurant/contact.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Account created.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'restaurant/register.html', {'form': form})


def login_view(request):
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


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')