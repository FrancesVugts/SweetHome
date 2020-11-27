from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Subscription
from houses.models import House
from .forms import UserProfileForm
from datetime import date


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    all_subscriptions = Subscription.objects.filter(user=profile.id)
    show = 'Info'

    today = str(date.today())
    active_subscriptions = all_subscriptions.filter(house__end_date__gte=today)
    subscriptions = active_subscriptions.filter(house__start_date__lte=today)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    for key, value in profile.__dict__.items():
        if key != "gender":
            if value is None:
                show = 'Form'

    if 'profile-update' in request.GET:
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


@login_required
def delete_subscription(request, subscription_id):
    """ Add the house to the subscriptions """

    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        subscription = get_object_or_404(Subscription, pk=subscription_id)
        subscription.delete()
        messages.success(request, 'Unsubscribed!')

    return redirect(redirect_url)
