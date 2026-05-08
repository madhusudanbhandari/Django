from django.urls import path
from . import views

urlpatterns = [
    path('',               views.home,           name='home'),
    path('about/',         views.about,          name='about'),
    path('menu/',          views.menu,           name='menu'),
    path('book-table/',    views.book_table,     name='book_table'),
    path('my-bookings/',   views.my_bookings,    name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('contact/',       views.contact,        name='contact'),
    path('register/',      views.register_view,  name='register'),
    path('login/',         views.login_view,     name='login'),
    path('logout/',        views.logout_view,    name='logout'),
]