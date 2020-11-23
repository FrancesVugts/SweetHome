from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import House, Type, City
from .forms import HouseForm
from datetime import date


def view_houses(request):
    """ A view to render the houses page """

    houses = House.objects.all()
    types = Type.objects.all()
    cities = City.objects.all()

    sortkey = None
    direction = None

    active_queries = None
    city_query = None
    min_pr_query = None
    max_pr_query = None
    price_queries = None
    type_query = None
    amount_query = None

    today = str(date.today())
    active_queries = Q(end_date__gte=today) & Q(start_date__lte=today)
    houses = houses.filter(active_queries)

    if 'sort' in request.GET:
        sort_request = request.GET['sort'].split(',')
        if sort_request[0] != "no_sorting":
            sortkey = sort_request[0]
            direction = sort_request[1]
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            houses = houses.order_by(sortkey)

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


@login_required
def add_house(request):
    """ Add a house """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only house management can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save()
            messages.success(request, 'Successfully added house!')
            return redirect(reverse('house_info', args=[house.id]))
        else:
            messages.error(request, 'Failed to add house. Please ensure the form is valid.')
    else:
        form = HouseForm()

    template = 'houses/add_house.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_house(request, house_id):
    """ Edit a house """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only house management can do that.')
        return redirect(reverse('home'))

    house = get_object_or_404(House, pk=house_id)
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated house!')
            return redirect(reverse('house_info', args=[house.id]))
        else:
            messages.error(request, 'Failed to update house. Please ensure the form is valid.')
    else:
        form = HouseForm(instance=house)
        messages.info(request, f'You are editing {house.address}')

    template = 'houses/edit_house.html'
    context = {
        'form': form,
        'house': house,
    }

    return render(request, template, context)


@login_required
def delete_house(request, house_id):
    """ Delete a house """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only house management can do that.')
        return redirect(reverse('home'))

    house = get_object_or_404(House, pk=house_id)
    house.delete()
    messages.success(request, 'House deleted!')
    return redirect(reverse('houses'))
