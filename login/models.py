from django.db import models

class Estudiante(models.Model):
    id_estudiante = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    tipo_id = models.CharField(max_length=25)
    nom_estudiante = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_estudiante = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    password_estudiante = models.CharField(max_length=255)

    class Meta:
        db_table = 'estudiantes'  # Nombre exacto de la tabla en la base de datos

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
        db_table = 'empresas'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.nom_empresa

class OfertaEmpleo(models.Model):
    id_oferta = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    nit = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='nit')
    nombre_oferta = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.TextField(max_length=1000)
    estado = models.BooleanField(default=True)  

    class Meta:
        db_table = 'ofertas_empleos' 

    def __str__(self):
        return self.nombre_oferta
