# Generated by Django 3.1.7 on 2021-04-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anunciosCachinaApp', '0005_auto_20210416_0744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='fecha',
            new_name='fecha_creation',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='fecha_modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
