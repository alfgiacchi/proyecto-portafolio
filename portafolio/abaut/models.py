from django.db import models

# modelo para formacion
class Course (models.Model):
    title = models.CharField(max_length=150,  verbose_name="Título")
    degree_title = models.CharField(max_length=150,  verbose_name="Descripcion obtenido")
    desccription = models.TextField(verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha modificación")
    
    class Meta:
        verbose_name="formación"
        verbose_name_plural = "formaciones"
        ordering = ['-created']
    
    def __str__(self):
        return self.title

# modelo para conocimientos

class Skill (models.Model):
    title = models.CharField(max_length=150,  verbose_name="Título")
    image = models.ImageField(upload_to='skills', verbose_name="Imagen")
    created =models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    update =models.DateTimeField(auto_now=True, verbose_name="Fecha modificación")

    class Meta:
        verbose_name="conocimiento"
        verbose_name_plural = "conocimientos"
        ordering = ['-created']
    
    def __str__(self):
        return self.title