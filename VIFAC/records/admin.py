from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Expediente)
class ExpedienteAdmin(admin.ModelAdmin): pass

