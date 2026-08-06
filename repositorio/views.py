from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "repositorio/home.html")

def nosotros(request):
    return render(request, "repositorio/nosotros.html")

def contacto(request):
    return render(request, "repositorio/contacto.html")