from django.shortcuts import render, get_object_or_404

from .models import UserProfile, Subscription
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    show = 'Info'
    subscriptions = Subscription.objects.filter(user=profile.id)

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
