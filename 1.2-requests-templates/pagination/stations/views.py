from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def reading_from_csv():
    with open('./data-398-2018-08-30.csv', 'r', encoding='UTF-8') as file:
        rows = csv.DictReader(file)
        my_data = [(row['Name'], row['Street'], row['District']) for row in rows]
    return my_data

MY_DATA = reading_from_csv()

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    pagi = Paginator(MY_DATA, 10)
    page_num = int((request.GET.get('page', 1)))
    pages = pagi.get_page(page_num)
    context = {
        'bus_stations': pages,
    }
    return render(request, 'stations/index.html', context)
