from django.shortcuts import render
from .models import Producto
# Create your views here.

def listar_productos(request):
    productos= Producto.objects.all()
    return render(request, "index.html", {"productos": productos})

