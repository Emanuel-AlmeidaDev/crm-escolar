# Generated by Django 4.0.4 on 2022-04-29 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('responsavel', '0001_initial'),
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='responsavel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='responsavel.responsavel'),
            preserve_default=False,
        ),
    ]
