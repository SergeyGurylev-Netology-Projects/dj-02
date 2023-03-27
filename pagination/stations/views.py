from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from csv import DictReader

with open(BUS_STATION_CSV, 'r', encoding="utf-8") as f:
    dict_reader = DictReader(f)
    CONTEXT = list(dict_reader)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    paginator = Paginator(CONTEXT, 10)
    page = paginator.get_page(int(request.GET.get('page', 1)))
    context = {
        'bus_stations': page.object_list,
        'page': page,
        'prev_numbers': [i for i in range(page.number - 3, page.number) if i > 0],
        'next_numbers': [i for i in range(page.number + 1, page.number + 4) if i <= paginator.num_pages],
        'num_pages': paginator.num_pages
    }

    return render(request, 'stations/index.html', context)
