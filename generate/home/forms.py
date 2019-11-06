from django import forms
from .models import (OptionGenerate,
                     Departament,
                     Directory)


MES = (
    ('01', 'Janeiro'),
    ('02', 'Fevereiro'),
    ('03', 'Março'),
    ('04', 'Abril'),
    ('05', 'Maio'),
    ('06', 'Junho'),
    ('07', 'Julho'),
    ('08', 'Agosto'),
    ('09', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro')
)

ANO = (
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19')
)


class DepartamentForm(forms.ModelForm):
    departament_name = forms.CharField(max_length=30, label='')

    class Meta:
        model = Departament
        fields = ['departament_name']


class DepartamentFormSelect(forms.ModelForm):
    departament_name = forms.ModelChoiceField(queryset=Departament.objects.all(), label='')

    class Meta:
        model = Departament
        fields = ['departament_name']


class GenerateForm(forms.ModelForm):
    client_name = forms.CharField(label='', max_length=100, required=True)
    departament_name = forms.ModelChoiceField(queryset=Departament.objects.all(), label='')
    mounth = forms.ChoiceField(choices=MES, label='', required=True)
    year = forms.ChoiceField(choices=ANO, label='', required=True)

    class Meta:
        model = OptionGenerate
        fields = ['client_name', 'departament_name', 'mounth', 'year']


class DirectoryForm(forms.ModelForm):
    departament_name = forms.ModelChoiceField(queryset=Departament.objects.all(), label='')
    name_program = forms.CharField(max_length=50, label='')
    description_program = forms.CharField(label='')
    directory_program = forms.CharField(label='')

    class Meta:
        model = Directory
        fields = ['departament_name', 'name_program', 'description_program', 'directory_program']