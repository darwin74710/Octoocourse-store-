from django.db import models
from django.db import models, connection



class Estudiante(models.Model):
    id_estudiante = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    tipo_id = models.CharField(max_length=25)
    nom_estudiante = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_estudiante = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    password_estudiante = models.CharField(max_length=255)

    class Meta:
        db_table = 'estudiantes'  

    def __str__(self):
        return f"{self.nom_estudiante} {self.apellido}"


class Empresa(models.Model):
    nit = models.DecimalField(primary_key=True, max_digits=25, decimal_places=0)
    nom_empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    correo_emp = models.CharField(max_length=50)
    password_emp = models.CharField(max_length=255)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        db_table = 'empresas'  

    def __str__(self):
        return self.nom_empresa



class OfertaEmpleo(models.Model):
    id_oferta = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    nit = models.DecimalField(max_digits=25, decimal_places=0)
    nombre_oferta = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.CharField(max_length=1000)
    estado = models.IntegerField()
    fecha_pub = models.DateField(auto_now_add=True)  


    class Meta:
        db_table = 'ofertas_empleos'

    def save(self, *args, **kwargs):
        if not self.id_oferta:  
            with connection.cursor() as cursor:
                cursor.execute("SELECT oferta_id_seq.NEXTVAL FROM dual")
                self.id_oferta = cursor.fetchone()[0]
        super(OfertaEmpleo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_oferta
    

class TipoCont(models.Model):
    id_tipo_cont = models.AutoField(primary_key=True)
    id_oferta = models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE, db_column='ID_OFERTA')
    tipo_cont = models.CharField(max_length=50)  


    class Meta:
        db_table = 'tipo_cont'
        constraints = [
            models.UniqueConstraint(fields=['id_tipo_cont', 'id_oferta'], name='pk_tipo_contrato')
        ]


class Conocimiento(models.Model):
    id_conocimiento = models.AutoField(primary_key=True)
    id_oferta = models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE, db_column='ID_OFERTA')
    nom_con = models.CharField(max_length=50)

    class Meta:
        db_table = 'conocimientos'


class HojasDeVida(models.Model):
    id_hoja_vida = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, db_column='ID_ESTUDIANTE')
    descripcion = models.TextField(max_length=1000)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)
    direccion = models.CharField(max_length=60)

    class Meta:
        db_table = 'hojas_de_vida'
    
    def __str__(self):
        return f"Hoja de Vida {self.id_hoja_vida} - Estudiante {self.id_estudiante}"


class LenguajesProg(models.Model):
    id_lenguaje = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_hoja_vida = models.ForeignKey(HojasDeVida, on_delete=models.CASCADE, db_column='ID_HOJAVIDA')
    nombre_leng = models.CharField(max_length=50)

    class Meta:
        db_table = 'lenguajes_prog'
    
    def __str__(self):
        return self.nombre_leng


class Aptitudes(models.Model):
    id_aptitudes = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_hoja_vida = models.ForeignKey(HojasDeVida, on_delete=models.CASCADE, db_column='ID_HOJAVIDA')
    nombre_apt = models.CharField(max_length=50)

    class Meta:
        db_table = 'aptitudes'
    
    def __str__(self):
        return self.nombre_apt


class Idiomas(models.Model):
    id_idioma = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_hoja_vida = models.ForeignKey(HojasDeVida, on_delete=models.CASCADE, db_column='ID_HOJAVIDA')
    idioma = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)

    class Meta:
        db_table = 'idiomas'
    
    def __str__(self):
        return f"{self.idioma} - Nivel {self.nivel}"


class FormacionesAcademicas(models.Model):
    id_formacion = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_hoja_vida = models.ForeignKey(HojasDeVida, on_delete=models.CASCADE, db_column='ID_HOJAVIDA')
    nom_institucion = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        db_table = 'formaciones_academicas'
    
    def __str__(self):
        return f"{self.titulo} - {self.nom_institucion}"


class ExpLaborales(models.Model):
    id_exp = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    id_hoja_vida = models.ForeignKey(HojasDeVida, on_delete=models.CASCADE, db_column='ID_HOJAVIDA')
    nom_empresas = models.CharField(max_length=50)
    tiempo_inicio = models.DateField()
    tiempo_final = models.DateField()
    cargo = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=1000)

    class Meta:
        db_table = 'exp_laborales'
    
    def __str__(self):
        return f"{self.cargo} en {self.nom_empresas}"
