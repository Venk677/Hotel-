from django.db import models
from django.db.models import CASCADE,DO_NOTHING
from datetime import date,timedelta

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_id=models.IntegerField()
    hotel_location=models.CharField(max_length=100)
    hotel_contact=models.IntegerField()
    no_of_rooms=models.IntegerField()

    def __str__(self):
        return self.hotel_name

class Manager(models.Model):
    hotel_manager_name=models.CharField(max_length=100)
    hotel_contact_no=models.IntegerField()
    hotel_manager_id=models.IntegerField()
    hotel_name=models.ForeignKey(Hotel, on_delete=CASCADE)


    def __str__(self):
        return self.hotel_manager_name

class Guest(models.Model):
    guest_name=models.CharField(max_length=100)
    guest_address=models.CharField(max_length=100)
    hotel_name=models.ForeignKey(Hotel,on_delete=CASCADE)
    guest_id=models.IntegerField()
    guest_contact=models.IntegerField()

    def __str__(self):
        return self.guest_name

class Room(models.Model):
    room_number=models.IntegerField()
    hotel_name=models.ForeignKey(Hotel,on_delete=CASCADE)
    guest_name=models.ForeignKey(Guest,on_delete=CASCADE)
    max_guests=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return str(self.room_number)

class Booking(models.Model):
    booking_id=models.IntegerField()
    hotel_name = models.ForeignKey(Hotel, on_delete=DO_NOTHING)
    hotel_manager_name=models.ForeignKey(Manager,on_delete=DO_NOTHING)
    guest_name = models.ForeignKey(Guest, on_delete=DO_NOTHING)
    room_number = models.IntegerField()
    log_in=models.DateField(auto_now_add=date.today())
    log_out=models.DateField(auto_now_add=date.today()+timedelta(days=1))
    total_price=models.IntegerField()
    is_cancelled=models.BooleanField()

# Create your models here.
