from django.test import SimpleTestCase
from profiles.forms import UserProfileForm


class TestForms(SimpleTestCase):

    def test_userprofile_form_valid_data(self):
        form = UserProfileForm(data={
            'initials': 'F.M.',
            'first_name': 'Frances',
            'last_name': 'Vugts',
            'address': 'address',
            'postcode': 'postcode',
            'city': 'city',
            'country': 'NL',
            'email': 'email@email.com',
            'phone_number': '06-12345678',
        })

        self.assertTrue(form.is_valid())

    def test_userprofile_form_no_data(self):
        form = UserProfileForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)
