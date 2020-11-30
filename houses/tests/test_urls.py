from django.test import SimpleTestCase
from django.urls import reverse, resolve
from houses.views import view_houses, house_info, add_house, edit_house, delete_house, del_subscription


# Used for example: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
class TestUrls(SimpleTestCase):

    def test_houses_url_resolves(self):
        url = reverse('houses')
        self.assertEquals(resolve(url).func, view_houses)

    def test_house_info_url_resolves(self):
        url = reverse('house_info', args=[1])
        self.assertEquals(resolve(url).func, house_info)

    def test_add_house_url_resolves(self):
        url = reverse('add_house')
        self.assertEquals(resolve(url).func, add_house)

    def test_edit_house_url_resolves(self):
        url = reverse('edit_house', args=[1])
        self.assertEquals(resolve(url).func, edit_house)

    def test_delete_house_url_resolves(self):
        url = reverse('delete_house', args=[1])
        self.assertEquals(resolve(url).func, delete_house)

    def test_del_subscription_url_resolves(self):
        url = reverse('del_subscription', args=[1])
        self.assertEquals(resolve(url).func, del_subscription)
