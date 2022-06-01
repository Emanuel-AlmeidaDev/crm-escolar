from django.contrib import admin
from .models import Responsavel

# Register your models here.

class ContratoInline(admin.TabularInline):
    model = Responsavel.contrato.through
    
@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ("name","status")
    inlines = [ContratoInline,]
    exclude = ['contrato',]

