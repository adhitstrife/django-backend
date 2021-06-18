from django.db import models

class Bookings(models.Model):
    pod_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    price = models.IntegerField()
    booking_date = models.DateField(auto_now_add=True)
    booking_time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ('booking_date',)
    
    def __str__(self):
        return self.user_name
    
    def get_absolute_url(self):
        return f'/{self.user_name}/'
    
