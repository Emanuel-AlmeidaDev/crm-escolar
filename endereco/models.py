from django.db import models

# Create your models here.
class Endereco(models.Model):
    description = models.TextField('Descrição')
    number = models.CharField('Número', max_length=10)
    neighborhood = models.CharField('Bairro', max_length=50)

    def __str__(this):
        return ', '.join([this.description, this.number, this.neighborhood])