# Generated by Django 4.2 on 2024-02-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('a_paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('a_materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('correo_electronico', models.CharField(max_length=50, verbose_name='Correo Electrónico')),
            ],
        ),
    ]
