from django import forms
from .models import OptionGenerate


class GenerateForm(forms.ModelForm):
    class Meta:
        model = OptionGenerate
        fields = ['client_name', 'departament_name', 'mounth', 'year']
