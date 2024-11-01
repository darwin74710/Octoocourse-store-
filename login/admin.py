from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Estudiante, Empresa, OfertaEmpleo

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante', 'nom_estudiante', 'apellido', 'correo_estudiante', 'fecha_nac')
    search_fields = ('nom_estudiante', 'apellido', 'correo_estudiante')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nom_empresa', 'correo_emp', 'telefono')
    search_fields = ('nom_empresa', 'correo_emp')

@admin.register(OfertaEmpleo)
class OfertaEmpleoAdmin(admin.ModelAdmin):
    list_display = ('id_oferta', 'nombre_oferta', 'salario', 'nit')
    search_fields = ('nombre_oferta', 'nit__nom_empresa')