from django.db import models
from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.
class Bebida(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    categoria = models.CharField(max_length=100, verbose_name="Categoría", help_text="Ej: Whisky, Ginebra, Tequila")
    descripcion = models.TextField(verbose_name="Descripción")
    especificaciones = models.CharField(max_length=300, verbose_name="Especificaciones", blank=True,
                                        help_text="Ej: Grados: 45% | Volumen: 750ml | Origen: Colombia")
    precio = models.CharField(max_length=50, verbose_name="Precio", help_text="Ej: $240.000")
    imagen = models.ImageField(upload_to='bebidas/', blank=True, null=True, verbose_name="Imagen")
    imagen_url = models.URLField(blank=True, verbose_name="URL de imagen externa",
                                 help_text="Usa esto si no subes imagen")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

    def __str__(self):
        return self.nombre
