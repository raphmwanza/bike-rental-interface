from django.core.management.base import BaseCommand
from bike_rental.models import BikeRentalBike

class Command(BaseCommand):
    help = 'Inserts predefined bikes into the BikeRentalBike model'

    def handle(self, *args, **kwargs):
        bikes = [
            ('Bike 1', 'Mountain', 10.0),
            ('Bike 2', 'Road', 12.5),
            ('Bike 3', 'Hybrid', 8.0),
            ('Bike 4', 'Cruiser', 15.0),
            ('Bike 5', 'Folding', 9.5),
            ('Bike 6', 'Electric', 14.0),
            ('Bike 7', 'Tandem', 13.0),
            ('Bike 8', 'Recumbent', 7.5),
            ('Bike 9', 'Fixed Gear', 11.0),
            ('Bike 10', 'Fat Bike', 5.5),
        ]

        for bike_name, bike_type, price in bikes:
            bike, created = BikeRentalBike.objects.get_or_create(
                bike_name=bike_name,
                bike_type=bike_type,
                price=price
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Bike "{bike_name}" inserted successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Bike "{bike_name}" already exists.'))

        self.stdout.write(self.style.SUCCESS('All bikes inserted.'))
