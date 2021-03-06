from django import forms
from .models import YearPayment


# Class to display a form based on the YearPayment model
class YearPaymentForm(forms.ModelForm):
    class Meta:
        model = YearPayment
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'city', 'postcode', 'country',)
        labels = {
            'street_address1': 'Address'
        }

    def __init__(self, *args, **kwargs):
        # Add placeholders and classes, remove auto-generated
        # labels and set autofocus on first field
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
