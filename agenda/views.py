from django.shortcuts import render
from .models import Agenda, Doctor, Paciente, Especialidad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import PacienteForm, DoctorForm, EspecialidadForm, AgendaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin

class RegistroUsuarioView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Usuario registrado exitosamente. Ahora puedes iniciar sesión.")
        return super().form_valid(form)

# =====================================
#  *VISTAS RELACIONADAS A ESPECIALIDAD
# =====================================

class EspecialidadListView(LoginRequiredMixin, ListView):
    model = Especialidad
    template_name = 'especialidad.list.html'
    context_object_name = 'especialidades'

class EspecialidadCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad_form.html'
    success_url = reverse_lazy('especialidad_list')
    success_message = "Especialidad agregada exitosamente."

class EspecialidadUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad_form.html'
    success_url = reverse_lazy('especialidad_list')
    success_message = "Especialidad actualizada exitosamente."

class EspecialidadDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Especialidad
    success_url = reverse_lazy('especialidad_list')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad eliminada correctamente")
        return super().form_valid(form)

# =====================================
#  *VISTAS RELACIONADAS A DOCTORES
# =====================================

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctores'

class DoctorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'
    success_url = reverse_lazy('doctor_list')
    success_message = "Doctor registrado correctamente."

class DoctorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'
    success_url = reverse_lazy('doctor_list')
    success_message = "Doctor actualizado exitosamente."

class DoctorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, "Doctor eliminado correctamente")
        return super().form_valid(form)

# =====================================
#  *VISTAS RELACIONADAS A PACIENTES
# =====================================

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'pacientes'

class PacienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente registrado correctamente."

class PacienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente actualizado exitosamente."

class PacienteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente_list')

    def form_valid(self, form):
        messages.success(self.request, "Paciente eliminado correctamente")
        return super().form_valid(form)

# =====================================
#  *VISTAS RELACIONADAS A AGENDA (CITA)
# =====================================

class AgendaListView(LoginRequiredMixin, ListView):
    model = Agenda
    template_name = 'agenda_list.html'
    context_object_name = 'citas'
    ordering = ['fecha', 'hora']

class AgendaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agenda_list')
    success_message = "Cita agendada exitosamente."

class AgendaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda_form.html'
    success_url = reverse_lazy('agenda_list')
    success_message = "Cita modificada correctamente."

class AgendaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')

    def form_valid(self, form):
        messages.success(self.request, "Cita cancelada/eliminada correctamente")
        return super().form_valid(form)