from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='doctores')
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Agenda(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='citas')
    hora = models.TimeField()
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} con {self.doctor}"