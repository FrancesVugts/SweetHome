from django.shortcuts import render, get_object_or_404
from .models import House, Type, City


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()
    types = Type.objects.all()
    cities = City.objects.all()
    city_name_query = None
    min_price_query = None
    max_price_query = None
    type_name_query = None
    amount_query = None

    if 'city_name' in request.GET:
        city_name_query = request.GET['city_name']
        if city_name_query == "all_cities":
            houses = houses
        else:
            houses = houses.filter(city__name__icontains=city_name_query)

    if 'min-price' and 'max-price' in request.GET:
        min_price_query = request.GET['min-price']
        max_price_query = request.GET['max-price']
        houses = houses.filter(price__gte=min_price_query) and houses.filter(price__lte=max_price_query)

    if 'type_name' in request.GET:
        type_name_query = request.GET['type_name']
        if type_name_query == "all_types":
            houses = houses
        else:
            houses = houses.filter(house_type__name__icontains=type_name_query)

    if 'amount' in request.GET:
        amount_query = request.GET['amount']
        if amount_query == "all_amounts":
            houses = houses
        else:
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
