# Generated by Django 3.1.7 on 2021-04-16 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anunciosCachinaApp', '0011_anuncio_categoria_subcategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoria',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Anuncio',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Subcategoria',
        ),
    ]
