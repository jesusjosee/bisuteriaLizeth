from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Descripción")
    link = models.URLField(verbose_name="link", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ['-created',]
        verbose_name="Nosotros"
        verbose_name_plural="Nosotros"

    def __str__(self):
        return self.title