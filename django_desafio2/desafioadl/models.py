from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)

    descripcion = models.CharField( max_length=250, default='' )
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)

    descripcion = models.CharField( max_length=250, default='' )
    eliminada = models.BooleanField(default=False)

    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.descripcion
