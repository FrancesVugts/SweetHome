from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Gender', choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], widget=forms.RadioSelect(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'initials': 'Initials',
    #         'first_name': 'First Name',
    #         'last_name': 'Last Name',
    #         'gender': '',
    #         'date_of_birth': 'Date of Birth',
    #         'address': 'Address',
    #         'postcode': 'Postal Code',
    #         'city': 'City',
    #         'email': 'Email',
    #         'phone_number': 'Phone Number',
    #     }

    #     self.fields['initials'].widget.attrs['autofocus'] = True
    #     for field in self.fields:
    #         if field != 'country':
    #             if self.fields[field].required:
    #                 placeholder = f'{placeholders[field]} *'
    #             else:
    #                 placeholder = placeholders[field]
    #             self.fields[field].widget.attrs['placeholder'] = placeholder
    #         self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
    #         self.fields[field].label = False
