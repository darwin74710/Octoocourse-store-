from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Estudiante, Empresa, OfertaEmpleo, TipoCont, Conocimiento, HojasDeVida, LenguajesProg, Aptitudes, Idiomas, FormacionesAcademicas, ExpLaborales, OfertaDisponible



class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_estudiante', 'nom_estudiante', 'apellido', 'correo_estudiante', 'fecha_nac')
    search_fields = ('nom_estudiante', 'apellido', 'correo_estudiante')

    def save_model(self, request, obj, form, change):
        if not obj.correo_estudiante.endswith('@elpoli.edu.co'):
            raise ValidationError(_("El correo electrónico debe terminar en '@elpoli.edu.co'."))
        
        super().save_model(request, obj, form, change)

admin.site.register(Estudiante, EstudianteAdmin)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nom_empresa', 'correo_emp', 'telefono')
    search_fields = ('nom_empresa', 'correo_emp')

@admin.register(OfertaEmpleo)
class OfertaEmpleoAdmin(admin.ModelAdmin):
    list_display = ('id_oferta', 'nombre_oferta', 'salario', 'nit')
    search_fields = ('nombre_oferta', 'nit')

    def delete_model(self, request, obj):
        OfertaDisponible.objects.filter(id_oferta=obj.id_oferta).delete()
        super().delete_model(request, obj)

@admin.register(TipoCont)
class TipoContAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_cont', 'nombre_tipo')  
    search_fields = ('nombre_tipo',)  


@admin.register(Conocimiento)
class ConocimientoAdmin(admin.ModelAdmin):
    list_display = ('id_conocimiento', 'id_oferta', 'nom_con')
    search_fields = ('nom_con', 'id_oferta__nombre_oferta')

@admin.register(HojasDeVida)
class HojasDeVidaAdmin(admin.ModelAdmin):
    list_display = ('id_hoja_vida', 'id_estudiante', 'telefono', 'direccion')
    search_fields = ('id_estudiante__nom_estudiante', 'direccion')


@admin.register(LenguajesProg)
class LenguajesProgAdmin(admin.ModelAdmin):
    list_display = ('id_lenguaje', 'id_hoja_vida', 'nombre_leng')
    search_fields = ('nombre_leng', 'id_hoja_vida__id_estudiante__nom_estudiante')


@admin.register(Aptitudes)
class AptitudesAdmin(admin.ModelAdmin):
    list_display = ('id_aptitudes', 'id_hoja_vida', 'nombre_apt')
    search_fields = ('nombre_apt', 'id_hoja_vida__id_estudiante__nom_estudiante')


@admin.register(Idiomas)
class IdiomasAdmin(admin.ModelAdmin):
    list_display = ('id_idioma', 'id_hoja_vida', 'idioma', 'nivel')
    search_fields = ('idioma', 'nivel', 'id_hoja_vida__id_estudiante__nom_estudiante')


@admin.register(FormacionesAcademicas)
class FormacionesAcademicasAdmin(admin.ModelAdmin):
    list_display = ('id_formacion', 'id_hoja_vida', 'nom_institucion', 'titulo', 'fecha_inicio', 'fecha_final')
    search_fields = ('nom_institucion', 'titulo', 'id_hoja_vida__id_estudiante__nom_estudiante')


@admin.register(ExpLaborales)
class ExpLaboralesAdmin(admin.ModelAdmin):
    list_display = ('id_exp', 'id_hoja_vida', 'nom_empresas', 'cargo', 'tiempo_inicio', 'tiempo_final')
    search_fields = ('nom_empresas', 'cargo', 'id_hoja_vida__id_estudiante__nom_estudiante')