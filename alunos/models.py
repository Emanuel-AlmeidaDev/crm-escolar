from django.db import models

# Create your models here.
class Aluno(models.Model):
    STATUS_TYPE = [
        ('AT','ATIVO'),
        ('AR','AGUARDANDO ROTA'),
        ('IN','INATIVO'),
    ]

    nome = models.CharField('Nome do aluno', max_length=50)
    address = models.ForeignKey('endereco.Endereco', on_delete=models.SET_NULL, null=True)
    responsavel = models.ForeignKey('responsavel.Responsavel', on_delete=models.CASCADE)
    horario_entrada = models.TimeField('Horário de entrada', auto_now=False, auto_now_add=False, null=True, blank=True)
    horario_saida = models.TimeField('Horário de entrada', auto_now=False, auto_now_add=False, null=True, blank=True)
    escola = models.ForeignKey('escola.Escola', on_delete=models.SET_NULL, null=True, default=None)
    status = models.CharField('Status', max_length=50, choices=STATUS_TYPE, default="IN", null=True)


    def __str__(this):
        return this.nome