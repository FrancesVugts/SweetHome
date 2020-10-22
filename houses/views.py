from django.shortcuts import render


def view_houses(request):
    """ A view to render the houses page """
    return render(request, 'houses/houses.html')
