from .models import Hotel
from .models import Hotel, Manager, Guest, Room, Booking
from django.contrib import admin
from django import forms


class HotelAdmin(admin.ModelAdmin):
    list_display = ( 'hotel_name', 'hotel_id', 'hotel_location', 'hotel_contact','no_of_rooms',)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('hotel_manager_name', 'hotel_contact_no', 'hotel_manager_id', 'hotel_name',)


class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'guest_address', 'hotel_name', 'guest_id', 'guest_contact',)


class RoomAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(RoomadminForm,self).__init__(*args,**kwargs)

    def clean(self):
        max_guests=self.cleaned_data.get("max_guests")
        if max_guests >= 3:
            raise forms.ValidationError("Maximum number of guests can only be 3")
        return self.cleaned_data


    def save(self, commit=True):
        return super(RoomadminForm,self).save(commit=commit)



class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel_name', 'guest_name', 'max_guests', 'price',)



class BookingAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookingAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        room_number = self.cleaned_data.get('room_number')
        if room_number == room_number:
            raise forms.ValidationError("Room Not Available")
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookingAdminForm, self).save(commit=commit)

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_id', 'hotel_name', 'hotel_manager_name', 'guest_name', 'room_number', 'log_in', 'log_out', 'total_price',
        'is_cancelled',)
    form=BookingAdminForm

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Booking, BookingAdmin)
