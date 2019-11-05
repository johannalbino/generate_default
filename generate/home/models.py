from django.db import models


SETOR = (
    ('1', 'Fiscal'),
    ('2', 'Contabil'),
    ('3', 'Materiais'),
    ('4', 'Financeiro'),
    ('5', 'NFCE')
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


class Departament(models.Model):
    departament_name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'DEPARTAMENT'

    def __str__(self):
        return self.departament_name


class OptionGenerate(models.Model):
    client_name = models.CharField(max_length=100)
    departament_name = models.ForeignKey(Departament, choices=SETOR, on_delete=models.PROTECT)
    mounth = models.CharField(max_length=16, choices=MES)
    year = models.CharField(max_length=2, choices=ANO)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'LOG_GENERATE'

    def __str__(self):
        return self.client_name


class Directory(models.Model):
    departament_name = models.ForeignKey(Departament, choices=SETOR, on_delete=models.PROTECT)
    name_program = models.CharField(max_length=50)
    description_program = models.TextField(blank=True, null=True)
    directory_program = models.TextField()

    class Meta:
        managed = True
        db_table = 'DIRECTORY_PROGRAM'

    def __str__(self):
        return self.name_program
