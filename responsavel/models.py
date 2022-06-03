from django.db import models

# Create your models here.
class Responsavel(models.Model):
    STATUS_TYPE = [
        ('AI','ATENDIMENTO INICIADO'),
        ('DM','DEMONSTROU INTERESSE'),
        ('DM','NÃO DEMONSTROU INTERESSE'),
        ('EN','EM NEGOCIAÇÃO'),
        ('AR','ASSINATURA REALIZADA'),
    ]

    name = models.CharField('Nome', max_length=100)
    phone = models.CharField("Número de telefone", max_length=20, null=True, blank=True)
    status = models.CharField('Status', max_length=2, choices=STATUS_TYPE, default="AI")
    comments = models.TextField('Comentários', null=True, blank="True")
    contrato = models.ManyToManyField('contratos.Contrato', verbose_name="Contrato")

    def __str__(this):
        return this.name