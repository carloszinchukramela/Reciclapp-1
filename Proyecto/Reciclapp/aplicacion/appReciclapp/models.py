from django.db import models


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


def __str__(self):
    return self.nombre
