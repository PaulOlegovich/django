import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    stations_list = []
    for row in reader:
        dist = {'Name': row['StationName'], 'Street': row['Street'], 'District': row['District']}
        stations_list.append(dist)

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
