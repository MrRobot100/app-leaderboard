from django.db import models

# Create your models here.
class Participante(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    puntaje=models.IntegerField(null=True)
    posicion_old=models.IntegerField(blank=True, null=True)
    posicion=models.IntegerField(blank=True, null=True)
    diff=models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre.upper() +' '+ self.apellido.upper()
