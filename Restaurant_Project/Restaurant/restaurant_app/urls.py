from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',               views.HomeView,           name='home'),
    path('about/',         views.AboutView,          name='about'),
    path('menu/',          views.MenuView,           name='menu'),
    path('book-table/',    views.BookTableView,     name='book_table'),
    path('my-bookings/',   views.MyBookingsView,    name='my_bookings'),
    path('cancel/<int:booking_id>/', views.CancelBookingView, name='cancel_booking'),
    path('contact/',       views.ContactView,        name='contact'),
    path('register/',      views.RegisterView,  name='register'),
    path('login/',         views.LoginView,     name='login'),
    path('logout/',        views.LogoutView,    name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)