# Generated by Django 5.0.7 on 2024-07-12 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeRentalBike',
            fields=[
                ('bike_id', models.AutoField(primary_key=True, serialize=False)),
                ('bike_name', models.TextField()),
                ('bike_type', models.TextField()),
                ('price', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BikeRentalUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('phone_number', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BikeRentalTransaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('rental_start_date', models.DateTimeField()),
                ('rental_end_date', models.DateTimeField()),
                ('bike_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_rental_interface.bikerentalbike')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_rental_interface.bikerentaluser')),
            ],
        ),
    ]
