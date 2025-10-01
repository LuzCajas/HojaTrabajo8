from django import forms
from .models import Estudiante, Administrador, Publicacion

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'escritor', 'autorizado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'escritor': forms.Select(attrs={'class': 'form-control'}),
            'autorizado': forms.Select(attrs={'class': 'form-control'}),
        }