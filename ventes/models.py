from django.db import models

from produitVariations.models import ProduitVariation


class Vente(models.Model):
    STATUS_CHOICES = [
        ('valide', 'Validée'),
        ('annule', 'Annulée'),
    ]

    # Définition des modes de paiement
    PAIEMENT_CHOICES = [
        ('especes', 'Espèces'),
        ('orange_money', 'Orange Money'),
        ('momo', 'Mobile Money (Momo)'),
    ]
    
    date_vente = models.DateTimeField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    client_nom = models.CharField(max_length=150, blank=True, null=True)
    methode_paiement = models.CharField(max_length=20, choices=PAIEMENT_CHOICES, default='ESPECES')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='valide')

    class Meta:
        db_table = "ventes"
        ordering = ['-date_vente']


    def annuler_vente(self):
        if self.status == 'valide':
            for ligne in self.lignes.all():
                ligne.variation.stock += ligne.quantite
                ligne.variation.save()
            self.status = 'annule'
            self.save()


class LigneVente(models.Model):
    vente = models.ForeignKey(Vente, related_name='lignes', on_delete=models.CASCADE)
    variation = models.ForeignKey(ProduitVariation, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta: 
        db_table = "ligne_ventes"


    def save(self, *args, **kwargs):
        if not self.id:
            self.variation.stock -= self.quantite
            self.variation.save()
        super().save(*args, **kwargs)
