from django import forms
from .models import Anuncio


class formPost(forms.ModelForm):
    #telefono = forms.IntegerField(label='telefono')

    class Meta:
        model = Anuncio
        fields = ['nombre',
                  'precio',
                  'ubicacion',
                  'descripcion',
                  'imagen',
                  'author',
                  'subcategoria',
                  ]
        #help_texts = {k:"" for k in fields}