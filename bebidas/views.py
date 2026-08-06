from django.shortcuts import render
from .models import Bebida

# Create your views here.

def bebidas(request):
    bebidas = Bebida.objects.all() 
    return render(request, 'bebidas/bebidas.html', {'bebidas': bebidas})