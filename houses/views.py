from django.shortcuts import render, get_object_or_404
from .models import House, City


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()
    cities = City.objects.all()
    city_name = None

    if 'city_name' in request.GET:
        city_name = request.GET['city_name'].split(',')
        houses = houses.filter(city__name__in=city_name)

    context = {
        'houses': houses,
        'cities': cities,
    }

    return render(request, 'houses/houses.html', context)


def house_info(request, house_id):
    """ A view to show the information about one specific house """

    house = get_object_or_404(House, pk=house_id)

    context = {
        'house': house,
    }

    return render(request, 'houses/house_info.html', context)
