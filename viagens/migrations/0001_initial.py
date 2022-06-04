# Generated by Django 4.0.4 on 2022-06-03 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0005_aluno_status_alter_aluno_horario_entrada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaViagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Data e Hora')),
                ('tipo', models.CharField(choices=[('I', 'IDA'), ('V', 'VOLTA'), ('T', 'TRANSLADO ALTERNATIVO')], max_length=2, verbose_name='Tipo')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.aluno')),
            ],
        ),
    ]