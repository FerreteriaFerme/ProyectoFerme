from django.contrib import admin
from .models import Marca , Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","herramienta","marca"]



admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)