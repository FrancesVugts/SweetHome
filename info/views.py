from django.shortcuts import render


def info(request):
    """ A view to return the index page """
    return render(request, 'info/info.html')
