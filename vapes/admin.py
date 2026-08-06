from django.contrib import admin
from .models import Vape

# Register your models here.

class VapeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'activo')
    list_filter = ('activo', 'categoria')
    search_fields = ('nombre',)
    list_editable = ('activo',)

admin.site.register(Vape, VapeAdmin)