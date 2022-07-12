from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    appaterno=models.CharField(max_length=50)
    apmaterno=models.CharField(max_length=50)
    edad=models.IntegerField()
    nom_vacuna=models.CharField(max_length=50)
    fecha=models.DateField()

class Vacunatorio(models.Model):
    id_atencion=models.IntegerField()
    nom_consultorio=models.CharField(max_length=50)
    nom_enfermero=models.CharField(max_length=50)
    rut_enfermero=models.CharField(max_length=9)
    nro_vacuna=models.IntegerField(max_length=2)
