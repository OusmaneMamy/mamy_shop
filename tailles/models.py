from django.db import models

# Create your models here.
class Taille(models.Model):
    nom = models.CharField(max_length=50)


    class Meta:
        db_table = "tailles"

    def __str__(self):
        return self.nom