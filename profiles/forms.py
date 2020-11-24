from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

    gender = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], widget=forms.RadioSelect(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'date_of_birth': 'YYYY-MM-DD',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'

        self.fields['initials'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'date_of_birth':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
