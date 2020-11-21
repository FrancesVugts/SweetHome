from django import forms
from .models import House, Type, City


class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = Type.objects.all()
        cities = City.objects.all()

        self.fields['type'].choices = types
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['city'].choices = cities
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
