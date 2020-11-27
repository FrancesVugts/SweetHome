from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import YearPaymentForm
from .models import YearPayment

import stripe


def payment(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    price = 25

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        payment_form = YearPaymentForm(form_data)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            payment.stripe_pid = pid
            payment.payment_total = price
            payment.save()
            return redirect(reverse('payment_success', args=[payment.payment_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        stripe_total = round(price * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        payment_form = YearPaymentForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'payment/payment.html'
    context = {
        'price': price,
        'payment_form': payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def payment_success(request, payment_number):
    """
    Handle successful payments
    """
    payment = get_object_or_404(YearPayment, payment_number=payment_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {payment_number}. A confirmation \
        email will be sent to {payment.email}.')

    template = 'payment/payment_success.html'
    context = {
        'payment': payment,
    }

    return render(request, template, context)
