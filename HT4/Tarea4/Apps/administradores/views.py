from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Administrador, Estudiante, Publicacion
from .forms import EstudianteForm, AdministradorForm, PublicacionForm
from django.urls import reverse_lazy
# Create your views here.

def ListarEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def ListarAdministradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'admin.html', {'administradores': administradores})

def ListarPublicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

class AcercaView(TemplateView):
    template_name = 'acerca.html'

class PubliView(TemplateView):
    template_name = 'publicaciones.html'

class CrearEstudiante(CreateView):
    template_name = 'crear_est.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('administradores:estudiantesapp')

class CrearAdmin(CreateView):
    template_name = 'crear_admin.html'
    form_class = AdministradorForm
    success_url = reverse_lazy('administradores:adminapp')

class CrearPublicaion(CreateView):
    template_name = 'crear_publi.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('administradores:publiapp')