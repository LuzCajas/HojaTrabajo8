from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.apellido, self.edad, self.ciudad)


class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.apellido, self.rol, self.ciudad)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    escritor = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    autorizado = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.titulo, self.fecha, self.contenido, self.escritor, self.autorizado)
