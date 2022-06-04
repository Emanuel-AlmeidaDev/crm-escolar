from django.db import models

# Create your models here.
class Contrato(models.Model):
    number = models.CharField('Número do contrato', max_length=50)
    file = models.FileField('Contrato (PDF)', upload_to='contratos', max_length=100)
    data_inicio = models.DateField('Data de início', auto_now=False, auto_now_add=False, null=True, blank=True)
    data_final = models.DateField('Último dia do contrato', auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return str(self.file.name)