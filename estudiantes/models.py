# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#Cargamos las tablas de la base de datos con "python manage.py inspectdb ESTUDIANTES APTITUDES CERTIFICADOS CURSOS CURSOS_APROBADOS DOC_ADMIN EXP_LABORALES FORMACIONES_ACADEMICAS HOJAS_DE_VIDA IDIOMAS LENGUAJES_PROG > .\estudiantes\models.py"

class Estudiantes(models.Model):
    id_estudiante = models.IntegerField(primary_key=True)
    tipo_id = models.CharField(max_length=25, blank=True, null=True)
    nom_estudiante = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    correo_estudiante = models.CharField(max_length=50, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    password_estudiante = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ESTUDIANTES'


class Aptitudes(models.Model):
    id_aptitudes = models.IntegerField(primary_key=True)
    id_hojavida = models.ForeignKey('HojasDeVida', models.DO_NOTHING, db_column='id_hojavida', blank=True, null=True)
    nombre_apt = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'APTITUDES'


class Certificados(models.Model):
    id_certificado = models.IntegerField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    id_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='id_curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CERTIFICADOS'


class Cursos(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nom_curso = models.CharField(max_length=50, blank=True, null=True)
    dificultad = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSOS'


class CursosAprobados(models.Model):
    id_aprobado = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURSOS_APROBADOS'


class DocAdmin(models.Model):
    id_docs_admin = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DOC_ADMIN'


class ExpLaborales(models.Model):
    id_exp = models.IntegerField(primary_key=True)
    id_hojavida = models.ForeignKey('HojasDeVida', models.DO_NOTHING, db_column='id_hojavida', blank=True, null=True)
    nom_empresas = models.CharField(max_length=50, blank=True, null=True)
    tiempo_inicio = models.DateField(blank=True, null=True)
    tiempo_final = models.DateField(blank=True, null=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EXP_LABORALES'


class FormacionesAcademicas(models.Model):
    id_formacion = models.IntegerField(primary_key=True)
    id_hojavida = models.ForeignKey('HojasDeVida', models.DO_NOTHING, db_column='id_hojavida', blank=True, null=True)
    nom_institucion = models.CharField(max_length=50, blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FORMACIONES_ACADEMICAS'


class HojasDeVida(models.Model):
    id_hoja_vida = models.IntegerField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiantes, models.DO_NOTHING, db_column='id_estudiante', blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HOJAS_DE_VIDA'


class Idiomas(models.Model):
    id_idioma = models.IntegerField(primary_key=True)
    id_hojavida = models.ForeignKey(HojasDeVida, models.DO_NOTHING, db_column='id_hojavida', blank=True, null=True)
    idioma = models.CharField(max_length=20, blank=True, null=True)
    nivel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IDIOMAS'


class LenguajesProg(models.Model):
    id_lenguaje = models.IntegerField(primary_key=True)
    id_hojavida = models.ForeignKey(HojasDeVida, models.DO_NOTHING, db_column='id_hojavida', blank=True, null=True)
    nombre_leng = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LENGUAJES_PROG'