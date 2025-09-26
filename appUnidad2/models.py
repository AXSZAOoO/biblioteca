from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(blank=True, null=True)
    numero_paginas = models.PositiveIntegerField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True, related_name='libros')

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo