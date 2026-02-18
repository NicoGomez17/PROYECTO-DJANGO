from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(models.CharField(max_length=100, unique=True))

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Paises"



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais_origen = models.ForeignKey(
        Pais, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Pais de origen"
    )

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.upper()}"
    
    class Meta:
        verbose_name_plural = "Clientes"