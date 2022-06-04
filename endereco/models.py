from django.db import models

# Create your models here.
class Endereco(models.Model):
    description = models.TextField('Descrição')
    number = models.CharField('Número', max_length=10, null=True, blank=True)
    neighborhood = models.CharField('Bairro', max_length=50)
    lat = models.CharField('Latitude', max_length=50, null=True, blank=True)
    lng = models.CharField('Longitude', max_length=50, null=True, blank=True)

    def __str__(this):
        return ', '.join([this.description, this.number, this.neighborhood])