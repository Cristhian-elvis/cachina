from django.shortcuts import render

# Create your views here.
from .models import Anuncio, Categoria, Subcategoria
from .forms import formPost
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    # return HttpResponse('Blog')
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.all()

    return render(
        request,
        'anunciosCachinaApp/home.html',
        {'anuncios': anuncios, 'categorias': categorias}
    )


def viewAnuncio(request, anuncio_id):

    anuncio = Anuncio.objects.get(id=anuncio_id)

    return render(
        request,
        'anunciosCachinaApp/vistaAnuncio.html',
        {'anuncio': anuncio}
    )

def misAnuncios(request):

    """return render(
        request,
        'anunciosCachinaApp/misAnuncios.html',
    )"""
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.all()

    return render(
        request,
        'anunciosCachinaApp/misAnuncios.html',
        {'anuncios': anuncios, 'categorias': categorias}
    )


def postStepOne(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'anunciosCachinaApp/postStep_one.html',
        {'categorias': categorias}
    )


def postStepTwo(request, id_category):
    categoria = Categoria.objects.get(id=id_category)
    subcategorias = Subcategoria.objects.all()

    return render(
        request,
        'anunciosCachinaApp/postStep_two.html',
        {'categoria': categoria, 'subcategorias': subcategorias}
    )


def postCreate(request, name_category, name_subcategory):
    subcategoria = Subcategoria.objects.get(nombre=name_subcategory)

    if request.method == 'POST':
        post = formPost(request.POST, files=request.FILES)
        if post.is_valid():
            post.save()
            return HttpResponseRedirect(reverse('Home'))
    else:
        post = formPost()
    return render(
        request,
        'anunciosCachinaApp/postCreate.html',
        {'subcategoria': subcategoria, 'post': post}
    )

def postUpdate(request, id_anounce):
    anuncio = Anuncio.objects.get(id=id_anounce)

    subcategoria = Subcategoria.objects.get(id=anuncio.subcategoria.id)

    if request.method == 'POST':
        post = formPost(request.POST, instance=anuncio, files=request.FILES)
        if post.is_valid():
            post.save()
            return HttpResponseRedirect(reverse('misAnuncios'))
    else:
        post = formPost(instance=anuncio)

    return render(
        request,
        'anunciosCachinaApp/postUpdate.html',
        {'subcategoria':subcategoria,'post': post}
    )

def postDelete(request, id_anounce):
    anuncio = Anuncio.objects.get(id=id_anounce)
    anuncio.delete()
    return HttpResponseRedirect(reverse('misAnuncios'))

# Pagina no encontrada
def pageNotFound(request):

    return render(
        request,
        'anunciosCachinaApp/pageNotFound.html'
    )
