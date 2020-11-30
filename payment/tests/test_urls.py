from django.test import SimpleTestCase
from django.urls import reverse, resolve
from payment.views import payment, payment_success


# Used for example: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
class TestUrls(SimpleTestCase):

    def test_payment_url_resolves(self):
        url = reverse('payment')
        self.assertEquals(resolve(url).func, payment)

    def test_payment_success_url_resolves(self):
        url = reverse('payment_success', args=[1])
        self.assertEquals(resolve(url).func, payment_success)
