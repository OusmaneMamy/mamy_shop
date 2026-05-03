from django.db import models

class Depense(models.Model):
    CATEGORIE_CHOICES = [
        ('loyer', 'Loyer'),
        ('electricite', 'Électricité / Eau'),
        ('transport', 'Transport / Logistique'),
        ('salaire', 'Salaires'),
        ('marketing', 'Publicité'),
        ('divers', 'Divers / Autres'),
    ]
    
    titre = models.CharField(max_length=200, verbose_name="Libellé de la dépense")
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, default='divers')
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    date_depense = models.DateField()
    description = models.TextField(blank=True, null=True)
    date_enregistrement = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "depenses"
        ordering = ['-date_depense']

    def __str__(self):
        return f"{self.titre} - {self.montant} GN"
