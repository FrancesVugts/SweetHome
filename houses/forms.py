from django import forms
from .widgets import CustomClearableFileInput
from .models import House


class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = '__all__'

    photo_1 = forms.ImageField(label='photo 1', required=False, widget=CustomClearableFileInput)
    photo_2 = forms.ImageField(label='photo 2', required=False, widget=CustomClearableFileInput)
    photo_3 = forms.ImageField(label='photo 3', required=False, widget=CustomClearableFileInput)
    photo_4 = forms.ImageField(label='photo 4', required=False, widget=CustomClearableFileInput)
    photo_5 = forms.ImageField(label='photo 5', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
