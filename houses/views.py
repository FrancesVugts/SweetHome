from django.shortcuts import render, get_object_or_404
from .models import House


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()

    context = {
        'houses': houses,
    }

    return render(request, 'houses/houses.html', context)


def house_info(request, house_id):
    """ A view to show the information about one specific house """

    house = get_object_or_404(House, pk=house_id)

    context = {
        'house': house,
    }

    return render(request, 'houses/house_info.html', context)
