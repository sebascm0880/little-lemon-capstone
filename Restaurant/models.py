from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.PositiveIntegerField()
    bookingdate = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.bookingdate.strftime('%Y-%m-%d %H:%M')}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - ${str(self.price)}"
