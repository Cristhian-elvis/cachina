from django.contrib import admin
from .models import Anuncio, Categoria, Subcategoria

# Register your models here.


# Register your models here.
class SubcategoriaAdmin(admin.ModelAdmin):
    pass

class CategoriaAdmin(admin.ModelAdmin):
    pass

class AnuncioAdmin(admin.ModelAdmin):
    pass
    #list_display = ("titulo","contenido")

admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Anuncio, AnuncioAdmin)
