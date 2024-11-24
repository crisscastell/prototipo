from django.shortcuts import render

# Create your views here.

def admin(request):
    return render(request, "admin.html")

def index(request):
    return render(request, "index.html")

def pacientes(request):
    return render(request, "pacientes.html")

def plantilla(request):
    return render(request, "plantilla.html")
    
def formularioMotivo(request):
    return render( request, "formularioMotivo.html")


