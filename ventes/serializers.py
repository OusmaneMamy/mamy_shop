from rest_framework import serializers
from .models import Vente, LigneVente

class LigneVenteSerializer(serializers.ModelSerializer):
    nomProduit = serializers.ReadOnlyField(source='variation.produit.nom')
    nomTaille = serializers.ReadOnlyField(source='variation.taille.nom')
    nomCouleur = serializers.ReadOnlyField(source='variation.couleur.nom')

    class Meta:
        model = LigneVente
        fields = ['id', 'variation', 'nomProduit', 'nomTaille', 'nomCouleur', 'quantite', 'prix_unitaire']

class VenteSerializer(serializers.ModelSerializer):
    lignes = LigneVenteSerializer(many=True, read_only=True)
    methode_paiement_display = serializers.CharField(source='get_methode_paiement_display', read_only=True)

    class Meta:
        model = Vente
        fields = ['id', 'date_vente', 'montant_total', 'client_nom', 'methode_paiement', 'methode_paiement_display', 'status', 'lignes']
    
    # NE PAS METTRE DE def create() ICI, ON LE FAIT DANS LA VIEW
