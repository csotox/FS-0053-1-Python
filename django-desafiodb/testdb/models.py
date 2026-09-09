from django.db import models

# Create your models here.
class Adltest(models.Model):
    campo1 = models.CharField( max_length=100 )
    valor1 = models.IntegerField()

    def __str__(self):
        return self.campo1

class AdlEjemplo(models.Model):
    campo1 = models.CharField( max_length=100 )
    valor1 = models.IntegerField()

    # testdb_adl_ejemplo
    class Meta:
        db_table = 'ejemplo_nombre_tabla'

    def __str__(self):
        return self.campo1
