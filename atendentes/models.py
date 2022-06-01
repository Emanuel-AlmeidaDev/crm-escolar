from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Atendente(User):

    class Meta:
        verbose_name_plural = "Atendente"
        verbose_name_plural = "Atendentes"

    def __str__(this):
        return this.first_name
