from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.reservation_date} {self.reservation_time.strftime('%H:%M:%S')}"

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    inventory = models.IntegerField()


    def __str__(self):
        return self.name
