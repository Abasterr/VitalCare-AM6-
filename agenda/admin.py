from django.contrib import admin
from datetime import date
from .models import Especialidad, Doctor, Paciente, Agenda


class PersonaAdmin(admin.ModelAdmin):
    @admin.display(description='edad')
    def get_edad(self, obj):
        today = date.today()
        return today.year - obj.fecha_nacimiento.year - ((today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Doctor)
class DoctorAdmin(PersonaAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'get_edad', 'especialidad')
    search_fields = ('nombre', 'apellido', 'especialidad__nombre')
    list_filter = ('especialidad',)
    
@admin.register(Paciente)
class PacienteAdmin(PersonaAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'get_edad')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nombre', 'apellido')
    
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'hora', 'fecha', 'motivo')
    autocomplete_fields = ('paciente', 'doctor')
    search_fields = ('paciente__nombre','paciente__apellido', 'doctor__nombre','doctor__apellido')
    list_filter = ('paciente', 'doctor', 'fecha')