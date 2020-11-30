from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, add_subscription, delete_subscription


# Used for example: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
class TestUrls(SimpleTestCase):

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_add_subscription_url_resolves(self):
        url = reverse('add_subscription', args=[1])
        self.assertEquals(resolve(url).func, add_subscription)

    def test_delete_subscription_url_resolves(self):
        url = reverse('delete_subscription', args=[1])
        self.assertEquals(resolve(url).func, delete_subscription)
