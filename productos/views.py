from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return redirect('listar_productos')
    return render(request, 'crear.html')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.cantidad = request.POST.get('cantidad')
        producto.save()
        return redirect('listar_productos')
    return render(request, 'editar.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar.html', {'producto': producto})
