from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def benefice(self):
        return self.prix_vente - self.prix_achat

    def __str__(self):
        return self.nom