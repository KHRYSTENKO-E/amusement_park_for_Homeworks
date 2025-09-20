from django.forms import ModelForm, NumberInput, TextInput
from main.models import Attractions


class AttractionForm(ModelForm):
    class Meta:
        model = Attractions
        fields = ["time", "name", "min_age", "zone"]
        widgets = {
            "time" : TextInput(attrs={
                'class' : 'form-control'
            }),
            "name": TextInput(attrs={
                'class': 'form-control'
            }),
            "min_age": NumberInput(attrs={
                'class': 'form-control'
            }),
            "zone": NumberInput(attrs={
                'class': 'form-control'
            }),
        }