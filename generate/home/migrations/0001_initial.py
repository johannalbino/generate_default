# Generated by Django 2.2.4 on 2019-08-13 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='optionsGerar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clienteName', models.CharField(max_length=100, verbose_name='Cliente')),
                ('setorName', models.CharField(choices=[('Fiscal', 'Fiscal'), ('Contabil', 'Contabil'), ('Materiais', 'Materiais'), ('Financeiro', 'Financeiro')], max_length=30, verbose_name='Setor')),
                ('mes', models.CharField(choices=[('01', 'Janeiro'), ('02', 'Fevereiro'), ('03', 'Março'), ('04', 'Abril'), ('05', 'Maio'), ('06', 'Junho'), ('07', 'Julho'), ('08', 'Agosto'), ('09', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'), ('12', 'Dezembro')], max_length=16, verbose_name='Mes')),
                ('ano', models.CharField(choices=[('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19')], max_length=2, verbose_name='Ano')),
            ],
        ),
    ]