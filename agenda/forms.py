from django import forms
from .models import Agenda, Doctor, Paciente, Especialidad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
        }

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fecha': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegistroAdminForm(UserCreationForm):
    es_administrador = forms.BooleanField(required=False, label="¿Dar permisos de administrador?", 
                                         widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email") # Campos que quieres mostrar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos las clases Pantone/Bootstrap a todos los campos de texto
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('es_administrador'):
            user.is_staff = True
            user.is_superuser = True 
        if commit:
            user.save()
        return user

es_administrador = forms.BooleanField(
    required=False, 
    label="¿Es Administrador?", 
    widget=forms.CheckboxInput(attrs={'id': 'id_es_administrador'})
)
