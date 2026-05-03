from django.db import models

# Create your models here.
class Couleur(models.Model):
    nom = models.CharField(max_length=50)


    class Meta:
        db_table = "couleurs"

    def __str__(self):
        return self.nom