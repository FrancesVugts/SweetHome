from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import House, Type, City
from datetime import date


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()
    types = Type.objects.all()
    cities = City.objects.all()

    active_queries = None
    city_query = None
    min_pr_query = None
    max_pr_query = None
    price_queries = None
    type_query = None
    amount_query = None

    today = today = str(date.today())
    active_queries = Q(end_date__gte=today) & Q(start_date__lte=today)
    houses = houses.filter(active_queries)

    if 'city_name' in request.GET:
        city_query = request.GET['city_name']
        if city_query != "all_cities":
            houses = houses.filter(city__name__icontains=city_query)

    if 'min-price' and 'max-price' in request.GET:
        min_pr_query = request.GET['min-price']
        max_pr_query = request.GET['max-price']
        price_queries = Q(price__gte=min_pr_query) & Q(price__lte=max_pr_query)
        houses = houses.filter(price_queries)

    if 'type_name' in request.GET:
        type_query = request.GET['type_name']
        if type_query != "all_types":
            houses = houses.filter(house_type__name__icontains=type_query)

    if 'amount' in request.GET:
        amount_query = request.GET['amount']
        if amount_query != "all_amounts":
            amount_query = int(amount_query)
            houses = houses.filter(bedrooms__gte=amount_query)

    context = {
        'houses': houses,
        'cities': cities,
        'types': types,
    }

    return render(request, 'houses/houses.html', context)


def house_info(request, house_id):
    """ A view to show the information about one specific house """

    house = get_object_or_404(House, pk=house_id)

    context = {
        'house': house,
    }

    return render(request, 'houses/house_info.html', context)
