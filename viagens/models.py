from django.db import models

# Create your models here.
class AgendaViagem(models.Model):

    TYPE_CHOICES = [
        ('I','IDA'),
        ('V','VOLTA'),
        ('T','TRANSLADO ALTERNATIVO'),
    ]

    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE)
    datetime = models.DateTimeField('Data e Hora', auto_now=False, auto_now_add=False)
    tipo = models.CharField('Tipo', choices=TYPE_CHOICES, max_length=2)

    class Meta:
        verbose_name_plural = "Agenda de viagens"

    def __str__(self):
        return ' '.join([str(self.datetime.strftime("%Y/%m/%d %H:%M")), self.aluno.nome])
