from django.shortcuts import render

from .forms import YearPaymentForm


def payment(request):
    payment_form = YearPaymentForm()
    template = 'payment/payment.html'
    context = {
        'payment_form': payment_form,
    }

    return render(request, template, context)
