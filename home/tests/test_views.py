from django.test import TestCase, Client
from django.urls import reverse


# used for examples: https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_view_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
