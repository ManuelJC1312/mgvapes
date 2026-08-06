from django.shortcuts import render
from .models import Vape

# Create your views here.

def vapes(request):
    lista = Vape.objects.filter(activo=True)
    return render(request, 'vapes/vapes.html', {'vapes': lista})
