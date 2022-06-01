from django.db import models

# Create your models here.
class Escola(models.Model):
    nome = models.CharField('Nome da escola', max_length=50)
    address = models.ForeignKey('endereco.Endereco', on_delete=models.CASCADE)

    def __str__(this):
        return this.nome