from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.user.models import UserProfile


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, null=False)
    contenido = models.TextField(null=False)
    resumen = models.TextField(max_length=600, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/post/publicado", default="media/post/default/default.jpg")
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True)
    permitir_comentarios = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-fecha_creacion","-fecha_actualizacion", "categoria"]  

    def __str__(self):
        return self.titulo
    
    def delete(self, *args):
        self.imagen.delete()
        super().delete(*args)


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(null=False)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True, null=True)


    class Meta:
        ordering = ["-fecha_creacion","-fecha_actualizacion"]

    def __str__(self):
        return self.contenido
    

