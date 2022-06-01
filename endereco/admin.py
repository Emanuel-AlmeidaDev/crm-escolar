from django.contrib import admin
from .models import Endereco
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Endereco)
# admin.site.unregister(User)
admin.site.unregister(Group)