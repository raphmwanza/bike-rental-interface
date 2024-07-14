from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("bike_rental_interface/", include("bike_rental_interface.urls")),
    path("admin/", admin.site.urls),
    path('', include('bike_rental.urls')),  # Include the bike_rental app's URLs
   
]