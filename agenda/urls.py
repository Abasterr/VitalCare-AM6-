from django.urls import path
from . import views

urlpatterns = [
    # Registro y Autenticación
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),

    # ESPECIALIDADES
    path('especialidades/', views.EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidades/nueva/', views.EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/editar/<int:pk>/', views.EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/eliminar/<int:pk>/', views.EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # DOCTORES
    path('doctores/', views.DoctorListView.as_view(), name='doctor_list'),
    path('doctores/nuevo/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', views.DoctorDeleteView.as_view(), name='doctor_delete'),

    # PACIENTES
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/eliminar/<int:pk>/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # AGENDA (CITAS)
    path('agenda/', views.AgendaListView.as_view(), name='agenda_list'),
    path('agenda/nueva/', views.AgendaCreateView.as_view(), name='agenda_create'),
    path('agenda/editar/<int:pk>/', views.AgendaUpdateView.as_view(), name='agenda_update'),
    path('agenda/eliminar/<int:pk>/', views.AgendaDeleteView.as_view(), name='agenda_delete'),
]
