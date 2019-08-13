from django import forms
from .models import OptionsGerar


class GerarForm(forms.ModelForm):
    class Meta:
        model = OptionsGerar
        fields = ['clienteName', 'setorName', 'mes', 'ano']
