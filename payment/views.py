from django.shortcuts import render

from .forms import YearPaymentForm


def payment(request):
    payment_form = YearPaymentForm()
    template = 'payment/payment.html'
    context = {
        'payment_form': payment_form,
        'stripe_public_key': 'pk_test_51HrVhrLnd5WhDuVG0W2hdN201C7BjKucLIvVqhT5t0pDLPy52NHQ13zQEsLldKKiML5Rrs1kogH9uUNfBaHE3gzj00hunWv5jj',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
