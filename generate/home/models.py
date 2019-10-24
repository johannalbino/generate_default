from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


SETOR = (
    ('Fiscal', 'Fiscal'),
    ('Contabil', 'Contabil'),
    ('Materiais', 'Materiais'),
    ('Financeiro', 'Financeiro')
)

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


class OptionsGerar(models.Model):
    clienteName = models.CharField(_('Cliente'), max_length=100)
    setorName = models.CharField(_('Setor'), max_length=30, choices=SETOR)
    mes = models.CharField(_('Mes'), max_length=16, choices=MES)
    ano = models.CharField(_('Ano'), max_length=2, choices=ANO)

    def __str__(self):
        return self.setorName


class OptionsGerar2(models.Model):
    clienteName = models.CharField(_('Cliente'), max_length=100)
    setorName = models.CharField(_('Setor'), max_length=30, choices=SETOR)
    mes = models.CharField(_('Mes'), max_length=16, choices=MES)
    ano = models.CharField(_('Ano'), max_length=2, choices=ANO)

    def __str__(self):
        return self.setorName


