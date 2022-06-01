from django.db import models

# Create your models here.
class Contrato(models.Model):
    number = models.CharField('Número do contrato', max_length=50)
    file = models.FileField('Contrato (PDF)', upload_to='contratos/media/', max_length=100)

    def __str__(self):
        return str(self.file.name)