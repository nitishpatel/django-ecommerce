"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from products.views import search
from addresses.views import checkout_address_create_view
app_name="main"
urlpatterns = [
    path('',views.home_page,name="homepage"),
    path('register',views.register,name="register"),
    path('logout',views.logout_request,name="logout"),
    path('login',views.login_request,name="login"),
    path('search/',search,name="search"),
    path('cart/guest/',views.guest_login_view,name="guest_login_view"),
    path('checkout/address/create',checkout_address_create_view,name="checkout_address_create")

    
]
