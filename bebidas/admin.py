from django.contrib import admin
from .models import Bebida

# Register your models here.
class BebidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'activo')
    list_filter = ('activo', 'categoria')
    search_fields = ('nombre',)
    list_editable = ('activo',)

admin.site.register(Bebida, BebidaAdmin)