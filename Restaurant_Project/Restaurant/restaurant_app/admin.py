from django.contrib import admin
from .models import MenuItem, Booking, ContactMessage
# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=['name','category','price','is_available']
    list_filter=['category','is_available']
    search_fields=['name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=['name','date','time','guests','email']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','created_at']