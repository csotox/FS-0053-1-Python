import uuid
from django.db import models
from django.db.models import ManyToManyField

# Modelo para clasificar cursos
class Clasi(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    nombre = models.CharField( max_length=50 )

    def __str__(self) -> str:
        return self.nombre

class Cursos(models.Model):
    id = models.AutoField(primary_key=True)

    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    nombre = models.CharField( max_length=150 )

    clasi = ManyToManyField(
        Clasi,
        related_name="Cursos"
    )

    def __str__(self) -> str:
        return self.nombre


"""
Ciclo de vida
-------------
1. Se crea o modifica un Modelo
2. Se ejecuta la migración
   python django_inicio/manage.py makemigrations
3. Se aplica la migración en la BBDD
   python django_inicio/manage.py migrate
"""
