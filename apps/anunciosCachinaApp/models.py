from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=15)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Anuncio(models.Model):
    nombre = models.CharField(max_length=30)
    #tipoAnuncio = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='blog')

    fecha_modificado = models.DateTimeField(auto_now=True)
    fecha_creation = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
