# Generated by Django 4.0.4 on 2022-06-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0006_alter_responsavel_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsavel',
            name='adress',
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número de telefone'),
        ),
    ]
