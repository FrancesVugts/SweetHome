from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile, Subscription
from houses.models import House
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    subscriptions = Subscription.objects.filter(user=profile.id)
    show = 'Info'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    for attr, value in profile.__dict__.items():
        if value is None:
            show = 'Form'

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'show': show,
        'subscriptions': subscriptions,
    }

    return render(request, template, context)


def add_subscription(request, house_id):
    """ Add the house to the subscriptions """

    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        user = get_object_or_404(UserProfile, user=request.user)
        house = get_object_or_404(House, pk=house_id)
        Subscription.objects.create(user=user, house=house)

    return redirect(redirect_url)
