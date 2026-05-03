from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


    class Meta:
        db_table = "produits"

        
    def __str__(self):
        return self.nom