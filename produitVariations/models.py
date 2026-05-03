from django.db import models
from couleurs.models import Couleur
from genres.models import Genre
from produits.models import Produit
from tailles.models import Taille

class ProduitVariation(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='variations')
    taille = models.ForeignKey(Taille, on_delete=models.SET_NULL, null=True, blank=True)
    couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    seuil_alerte = models.IntegerField(default=5)


    class Meta:
        db_table = "produitVariations"
        unique_together = ['produit', 'taille', 'genre', 'couleur']


    def benefice(self):
        return self.prix_vente - self.prix_achat

    def __str__(self):
        return f"{self.produit.nom} - {self.taille.nom} - {self.couleur.nom} - {self.genre.nom}"