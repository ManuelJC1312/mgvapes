from django.contrib import admin
from .models import Mensaje


class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha', 'leido')
    list_filter = ('leido',)
    list_editable = ('leido',)
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'fecha')
