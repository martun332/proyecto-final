from django.db import models

# Create your models here.

class prueba(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()