from django.db import models
from datetime import date

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

# --- CLASE BASE PARA EDAD (DRY) ---
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    class Meta:
        abstract = True

    def calcular_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

# --- MODELOS QUE HEREDAN DE PERSONA ---
class Doctor(Persona):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='doctores')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paciente(Persona):
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Agenda(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('R', 'Realizada'),
        ('C', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    hora = models.TimeField()
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} con {self.doctor}"
