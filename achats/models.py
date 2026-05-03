from django.db import models
from produitVariations.models import ProduitVariation

class Achat(models.Model):
    STATUT_CHOICES = [
        ('recu', 'Reçu'),
        ('en_attente', 'En attente'),
        ('annule', 'Annulé'),
    ]
    
    date_achat = models.DateTimeField(auto_now_add=True)
    fournisseur = models.CharField(max_length=150, blank=True, null=True)
    montant_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='recu')


    class Meta:
        db_table = "achats"
        ordering = ['-date_achat']

    def __str__(self):
        return f"Achat #{self.id} - {self.fournisseur}"




class LigneAchat(models.Model):
    achat = models.ForeignKey(Achat, related_name='lignes', on_delete=models.CASCADE)
    variation = models.ForeignKey(ProduitVariation, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField()
    prix_achat_unitaire = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        db_table = "ligne_achats"

    def save(self, *args, **kwargs):
        # LOGIQUE : On AUGMENTE le stock lors d'un achat
        if not self.id:
            self.variation.stock += self.quantite
            self.variation.save()
        super().save(*args, **kwargs)
