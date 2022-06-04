# Generated by Django 4.0.4 on 2022-06-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='lng',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
    ]
