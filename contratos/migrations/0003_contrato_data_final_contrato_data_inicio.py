# Generated by Django 4.0.4 on 2022-06-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_alter_contrato_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='data_final',
            field=models.DateField(blank=True, null=True, verbose_name='Último dia do contrato'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início'),
        ),
    ]
