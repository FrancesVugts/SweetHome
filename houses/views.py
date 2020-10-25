from django.shortcuts import render
from .models import House


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()

    context = {
        'houses': houses,
    }

    return render(request, 'houses/houses.html', context)
