# Generated by Django 3.1.7 on 2021-04-16 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anunciosCachinaApp', '0010_auto_20210416_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anunciosCachinaApp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.BooleanField(default=True)),
                ('ubicacion', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='blog')),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('fecha_creation', models.DateTimeField(auto_now_add=True)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anunciosCachinaApp.subcategoria')),
            ],
        ),
    ]
