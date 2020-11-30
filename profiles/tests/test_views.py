from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


# used for examples: https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')

    def test_view_profile_GET(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
