from django.shortcuts import render,redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from core.models import Producto
from django.contrib.auth.decorators import login_required ,permission_required




# Create your views here.
def Index (request):
    return render(request,'app/Index.html')

def Prueba(request):
    return render(request, 'app/prueba.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
  
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login (request, user)
            messages.success(request, "Te has registrado correctamente.")
            return redirect(to= "Index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto guardado correctamente.")
            return redirect(to= "menu-productos")
        else:
            data["form"] = formulario
    
    return render(request,'app/productos/agregar.html',data)

def menu_productos(request):
    return render(request, 'app/productos/menu.html')

def listar_productos(request):
    productos = Producto.objects.all()

    data={
        'productos': productos
    }
    return render(request, 'app/productos/listar.html', data)

def modificar_producto(request,id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente.")
            return redirect(to= "listar-productos")
            

    return render(request, 'app/productos/modificar.html',data)

def eliminar_productos(request ,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return redirect(to= "listar-productos")

def listado_productos(request):
    productos = Producto.objects.all()

    data={
        'productos': productos
    }
    return render(request, 'app/vista_cliente/listado_productos.html', data)