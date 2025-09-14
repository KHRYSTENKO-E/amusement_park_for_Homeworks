from django.http import HttpResponse
from django.shortcuts import render
from .models import Attractions


def show_main_page(request):
    return render(request, "main/main_page.html")

def show_contacts(request):
    return render(request, "main/contacts.html")

def show_about(request):
    return render(request, "main/about.html")

def show_prices(request):
    return render(request, "main/prices.html")

def show_attractions(request):
        all_attractions = Attractions.objects.all()
        count_of_attractions = len(all_attractions)
        return render(request, "main/attractions.html", {'attractions': all_attractions, "count" : count_of_attractions})
