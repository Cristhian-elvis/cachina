from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.decorators import login_required
from .models import Anuncio, Categoria

#@login_required
def home(request):
    #return HttpResponse('Blog')
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.all()

    return render(
        request, 
        'anunciosCachinaApp/home.html', 
        {'anuncios':anuncios, 'categorias':categorias}
    )
