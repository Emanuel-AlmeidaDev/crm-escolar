# Generated by Django 4.0.4 on 2022-04-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('number', models.CharField(max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro')),
            ],
        ),
    ]
