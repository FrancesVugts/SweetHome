from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Subscription
from houses.models import House
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    subscriptions = Subscription.objects.filter(user=profile.id)
    show = 'Info'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    for attr, value in profile.__dict__.items():
        if value is None:
            show = 'Form'

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'show': show,
        'subscriptions': subscriptions,
    }

    return render(request, template, context)


@login_required
def add_subscription(request, house_id):
    """ Add the house to the subscriptions """

    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        user = get_object_or_404(UserProfile, user=request.user)
        house = get_object_or_404(House, pk=house_id)
        subscriptions = Subscription.objects.all()
        alreadyExists = False

        for subscription in subscriptions:
            if user == subscription.user and house == subscription.house:
                alreadyExists = True

        if not alreadyExists:
            Subscription.objects.create(user=user, house=house)

    return redirect(redirect_url)
