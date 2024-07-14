# bike_rental/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import BikeRentalBike, BikeRentalTransaction
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'bike_rental/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('home')
    return render(request, 'bike_rental/signup.html')


@login_required
def home_view(request):
    username = request.user.username

    bikes = BikeRentalBike.objects.all()
    rentals = BikeRentalTransaction.objects.filter(user_id=request.user.bikerentaluser)
    
    return render(request, 'bike_rental/home.html', {'bikes': bikes, 'rentals': rentals, 'username': username})

def logout_view(request):
    logout(request)
    return redirect('login')








def rent_bike(request, bike_id):
    if request.method == 'POST':
        rental = BikeRentalTransaction(
            transaction_date=timezone.now(),
            rental_start_date=timezone.now(),
            rental_end_date=timezone.now() + timezone.timedelta(days=1),
            bike_id=bike_id,
            user_id=request.user.id
        )
        rental.save()
        return redirect('success_page')  # Redirect to a success page or wherever you want
def home_view(request):
    return render(request, 'home.html')