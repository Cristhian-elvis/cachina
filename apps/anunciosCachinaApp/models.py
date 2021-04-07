from django.db import models

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
    tipoAnuncio = models.CharField(max_length=10)
    precio = models.FloatField()
    estado = models.BooleanField()
    ubicacion = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField()

    fecha = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
