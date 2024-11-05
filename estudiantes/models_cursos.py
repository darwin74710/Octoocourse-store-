# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cursos(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nom_curso = models.CharField(max_length=50, blank=True, null=True)
    dificultad = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    url_imagen = models.CharField(max_length=1000, blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    lenguaje = models.CharField(max_length=25, blank=True, null=True)
    tiempo = models.CharField(max_length=15, blank=True, null=True)
    certificado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSOS'


class CursosDisponibles(models.Model):
    id_cur_disponible = models.AutoField(primary_key=True)
    activacion = models.BooleanField(blank=True, null=True)
    id_estudiante = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSOS_DISPONIBLES'


class CursosAprobados(models.Model):
    id_aprobado = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_estudiante = models.ForeignKey('Estudiantes', models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSOS_APROBADOS'


class Contenidos(models.Model):
    id_contenido = models.IntegerField(primary_key=True)
    nom_contenido = models.CharField(max_length=50, blank=True, null=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONTENIDOS'


class SubContenidos(models.Model):
    id_subcont = models.IntegerField(primary_key=True)
    nom_subcont = models.CharField(max_length=50, blank=True, null=True)
    url_cont = models.CharField(max_length=1000, blank=True, null=True)
    id_contenido = models.ForeignKey(Contenidos, models.DO_NOTHING, db_column='id_contenido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SUB_CONTENIDOS'


class PreguntasCurso(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    pregunta_text = models.CharField(max_length=1000, blank=True, null=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PREGUNTAS_CURSO'


class RespuestasCurso(models.Model):
    id_respuesta = models.IntegerField(primary_key=True)
    respuesta_text = models.CharField(max_length=1000, blank=True, null=True)
    validacion = models.BooleanField(blank=True, null=True)
    id_pregunta = models.ForeignKey(PreguntasCurso, models.DO_NOTHING, db_column='id_pregunta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RESPUESTAS_CURSO'