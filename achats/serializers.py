from rest_framework import serializers
from .models import Achat, LigneAchat

class LigneAchatSerializer(serializers.ModelSerializer):
    nomProduit = serializers.ReadOnlyField(source='variation.produit.nom')
    nomTaille = serializers.ReadOnlyField(source='variation.taille.nom')

    class Meta:
        model = LigneAchat
        fields = ['id', 'variation', 'nomProduit', 'nomTaille', 'quantite', 'prix_achat_unitaire']

class AchatSerializer(serializers.ModelSerializer):
    # read_only=True est crucial ici pour que is_valid() ne rejette pas le champ 'lignes'
    lignes = LigneAchatSerializer(many=True, read_only=True)

    class Meta:
        model = Achat
        fields = ['id', 'date_achat', 'fournisseur', 'montant_total', 'statut', 'lignes']
