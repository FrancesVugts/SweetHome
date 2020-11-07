from django.shortcuts import render, get_object_or_404
from .models import House, Type, City


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()
    types = Type.objects.all()
    cities = City.objects.all()
    city_name_query = None
    type_name_query = None

    if 'city_name' in request.GET:
        city_name_query = request.GET['city_name']
        houses = houses.filter(city__name__icontains=city_name_query)

    if 'type_name' in request.GET:
        type_name_query = request.GET['type_name']
        houses = houses.filter(house_type__name__icontains=type_name_query)

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
