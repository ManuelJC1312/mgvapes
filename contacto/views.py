from django.shortcuts import render, redirect
from .models import Mensaje


def contacto(request):
    enviado = False

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        asunto = request.POST.get('asunto', '').strip()
        mensaje_texto = request.POST.get('mensaje', '').strip()

        if nombre and email and asunto and mensaje_texto:
            Mensaje.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje_texto
            )
            enviado = True

    return render(request, 'contacto/contacto.html', {'enviado': enviado})
