from django.test import TestCase, Client
from django.urls import reverse


# used for examples: https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.info_url = reverse('info')

    def test_view_info_GET(self):
        response = self.client.get(self.info_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/info.html')
