# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Conocimientos(models.Model):
    id_conocimiento = models.IntegerField(primary_key=True)
    id_oferta = models.ForeignKey('OfertasEmpleos', models.DO_NOTHING, db_column='id_oferta')
    nom_con = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONOCIMIENTOS'


class OfertasEmpleos(models.Model):
    id_oferta = models.IntegerField(primary_key=True)
    nit = models.BigIntegerField(blank=True, null=True)
    nombre_oferta = models.CharField(max_length=50, blank=True, null=True)
    salario = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OFERTAS_EMPLEOS'


class TipoCont(models.Model):
    id_tipo_cont = models.IntegerField(primary_key=True)  # The composite primary key (id_tipo_cont, id_oferta) found, that is not supported. The first column is selected.
    id_oferta = models.ForeignKey(OfertasEmpleos, models.DO_NOTHING, db_column='id_oferta')

    class Meta:
        managed = False
        db_table = 'TIPO_CONT'
        unique_together = (('id_tipo_cont', 'id_oferta'),)