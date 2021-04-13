from django.db import models

# Create your models here.
class Comuna(models.Model):
    nombre= models.CharField(max_length=50)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    comuna = models.ForeignKey(Comuna, on_delete= models.PROTECT)

class Marca(models.Model):
    nombre =  models.CharField (max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    herramienta = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete =models.PROTECT)
    imagen = models.ImageField(upload_to = "productos",null= True)
    def __str__(self):
        return self.nombre

 

    
    