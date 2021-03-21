from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="women")
    link = models.URLField(verbose_name="link", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ['-created',]
        verbose_name="Pulseras para mujeres"
        verbose_name_plural="Pulseras para mujeres"

    def __str__(self):
        return self.title

class Men(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="men")
    link = models.URLField(verbose_name="link", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ['-created',]
        verbose_name="Pulseras para hombre"
        verbose_name_plural="Pulseras para hombres"

    def __str__(self):
        return self.title

class Couple(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="cuople")
    link = models.URLField(verbose_name="link", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ['-created',]
        verbose_name="Pulseras para pareja"
        verbose_name_plural="Pulseras para parejas"

    def __str__(self):
        return self.title


