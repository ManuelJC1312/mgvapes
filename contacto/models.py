from django.db import models

# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo electrónico")
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False, verbose_name="Leído")

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
