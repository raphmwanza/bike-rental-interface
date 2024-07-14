from django.db import models
from django.contrib.auth.models import User

class BikeRentalUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

class BikeRentalBike(models.Model):
    bike_id = models.AutoField(primary_key=True)
    bike_name = models.TextField()
    bike_type = models.TextField()
    price = models.FloatField()
    is_available = models.BooleanField(default=True)

    def rent(self, user, rental_start_date, rental_end_date):
        if self.is_available:
            self.is_available = False
            self.save()
            BikeRentalTransaction.objects.create(
                rental_start_date=rental_start_date,
                rental_end_date=rental_end_date,
                bike_id=self,
                user_id=user
            )
            return True
        return False

class BikeRentalTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    rental_start_date = models.DateTimeField()
    rental_end_date = models.DateTimeField()
    bike_id = models.ForeignKey(BikeRentalBike, on_delete=models.CASCADE)
    user_id = models.ForeignKey(BikeRentalUser, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.pk:  # Only set these fields on creation
            self.bike_name = self.bike_id.bike_name
            self.bike_type = self.bike_id.bike_type
        super().save(*args, **kwargs)

    def return_bike(self):
        from django.utils import timezone
        if not self.bike_id.is_available:
            self.bike_id.is_available = True
            self.bike_id.save()
            self.rental_end_date = timezone.now()
            self.save()
            return True
        return False
