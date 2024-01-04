from django.db import models

class Booking(models.Model):
    ID1 = models.IntegerField(default=2)
    Name = models.CharField(max_length=255, default=" ")
    No_of_guests = models.IntegerField(default=1)
    BookingdDate = models.DateTimeField()




class Menu(models.Model):
    ID2 = models.IntegerField(default=1)
    Title = models.CharField(max_length=255, default=" ")
    Price = models.FloatField(default=10.2)
    Inventory = models.IntegerField(default=1)

# Create your models here.
