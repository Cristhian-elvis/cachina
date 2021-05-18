from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=30)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Anuncio(models.Model):
    nombre = models.CharField(max_length=30)
    #tipoAnuncio = models.CharField(max_length=10)
    precio = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='anuncios')

    fecha_modificado = models.DateTimeField(auto_now=True)
    fecha_creation = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)

    def getPrecio(self):
        priceConverter = ''
        if self.precio>999:
            priceConverter += str(self.precio//1000)
            if self.precio%1000 == 0:
                priceConverter += ',000'
            else:
                priceConverter += ',' + str(self.precio%1000)
            
            return priceConverter
        return self.precio

    def isFree(self):
        if self.precio == 0:
            return True
        return False


    def __str__(self):
        return self.nombre
