from django.test import SimpleTestCase
from django.urls import reverse, resolve
from info.views import info


# Used for example: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
class TestUrls(SimpleTestCase):

    def test_info_url_resolves(self):
        url = reverse('info')
        self.assertEquals(resolve(url).func, info)
