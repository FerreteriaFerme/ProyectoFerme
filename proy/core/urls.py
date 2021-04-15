from django.urls import path
from .views import  Index, Prueba , registro, agregar_producto,menu_productos
from .views import listar_productos, modificar_producto, eliminar_productos, listado_productos
urlpatterns = [
    path('', Index, name= "Index"),
    path('Prueba', Prueba, name= "Prueba"),
    path('Prueba', Prueba, name= "Prueba"),
    path('registro/', registro, name= "registro"),
    path('agregar-productos/', agregar_producto, name= "agregar_producto"),
    path('menu-productos/', menu_productos, name= "menu-productos"),
    path('listar-productos/', listar_productos, name= "listar-productos"),
    path('modificar-productos/<id>/', modificar_producto, name= "modificar-productos"),
    path('eliminar-productos/<id>/', eliminar_productos, name= "eliminar-productos"),
    path('listado_productos', listado_productos, name = 'listado-productos')
]
