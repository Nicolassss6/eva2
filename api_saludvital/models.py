from django.db import models

# Create your models here.
from django.db import models

# -------------------------------
# MODELOS BASE SALUD VITAL LTDA.
# -------------------------------

# Opción 1 de mejora: CHOICES
GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]

# Opción 2 de mejora: nueva tabla EstadoConsulta
class EstadoConsulta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad.nombre}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.ForeignKey(EstadoConsulta, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente.nombre} con {self.medico.nombre}"


class Tratamiento(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    duracion_dias = models.PositiveIntegerField()

    def __str__(self):
        return f"Tratamiento {self.id} - {self.consulta.paciente.nombre}"


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    dosis_recomendada = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    indicaciones = models.TextField()
    fecha_emision = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Receta para {self.consulta.paciente.nombre}"
