# Generated by Django 4.0.4 on 2022-06-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_alter_contrato_file'),
        ('responsavel', '0005_responsavel_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsavel',
            name='comments',
            field=models.TextField(blank='True', null=True, verbose_name='Comentários'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='contrato',
            field=models.ManyToManyField(to='contratos.contrato', verbose_name='Contrato'),
        ),
    ]
