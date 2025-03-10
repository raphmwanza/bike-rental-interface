"""
URL configuration for bike_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path
from bike_rental_interface.views import login_view, signup_view, home_view, logout_view, rent_bike_view






urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('return/<int:transaction_id>/', rent_bike_view, name='home'),

]
