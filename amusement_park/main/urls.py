from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_main_page),
    path('contacts', views.show_contacts, name = "contacts"),
    path('about', views.show_about, name = "about"),
    path('prices', views.show_prices, name = "prices"),
]