from django.db import models
from django.db.models import CASCADE,DO_NOTHING
from datetime import date,timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_location=models.CharField(max_length=100)
    hotel_contact=models.CharField(max_length=10)
    no_of_rooms=models.IntegerField()

    def __str__(self):
        return self.hotel_name

class Manager(models.Model):
    hotel_manager_name=models.CharField(max_length=100)
    manager_contact_no=models.CharField(max_length=10)
    hotel_manager_id=models.IntegerField()
    hotel_name=models.ForeignKey(Hotel,on_delete=CASCADE)


    def __str__(self):
        return self.hotel_manager_name

class Guest(models.Model):
    guest_name=models.CharField(max_length=100)
    guest_address=models.CharField(max_length=100)
    hotel_name=models.ForeignKey(Hotel,on_delete=CASCADE)
    guest_contact=models.CharField(max_length=10)

    def __str__(self):
        return self.guest_name

class Room(models.Model):
    room_number=models.IntegerField(primary_key=True)
    hotel_name=models.ForeignKey(Hotel,on_delete=CASCADE)
    max_guests=models.IntegerField()
    price=models.IntegerField()
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_number)



class Booking(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=DO_NOTHING)
    hotel_manager_name=models.ForeignKey(Manager,on_delete=DO_NOTHING)
    guest_name = models.ForeignKey(Guest, on_delete=DO_NOTHING)
    room_number = models.ForeignKey(Room,on_delete=DO_NOTHING)
    log_in = models.DateField(default=date.today())
    log_out = models.DateField(default=date.today()+timedelta(days=1))
    check_out = models.BooleanField(default=False)
    # is_cancelled=models.BooleanField()

    @property
    def total_price(self):
        price1=self.room_number.price
        total =(self.log_out - self.log_in).days
        total_price=total*price1
        return total_price

@receiver(post_save,sender=Booking)
def update_available(sender,created,instance,**kwargs):
    room_number=instance.room_number
    if created:
        room_number.available = False
        room_number.save()
    elif not instance.check_out:
        room_number.available = True
        room_number.save()

# Create your models here.
