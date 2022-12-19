from django.shortcuts import render
from .models import Cliente

# Create your views here.
def crearCliente(request):
    vendedor1=Cliente(nombre="Mateo", apellido="Marsili", cargo="Vendedor Zona Norte")
    vendedor1.save()
    cadena= f"La venta se asigno correctamente a {vendedor1.nombre} {vendedor1.apellido} y su cargo es: {vendedor1.cargo}"
    return render(request, "AppCoder/vendedores.html")