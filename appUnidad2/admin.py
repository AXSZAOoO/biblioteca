from django.contrib import admin
from .models import Autor, Libro, Editorial

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'nacionalidad')

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'direccion')
    search_fields = ('nombre', 'pais')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'fecha_publicacion', 'numero_paginas')
    list_filter = ('editorial',)
    search_fields = ('titulo', 'autor__nombre', 'autor__apellido')