# from rest_framework import serializers
# from .models import ProduitVariation

# class ProduitVariationSerializer(serializers.ModelSerializer):
#     benefice = serializers.SerializerMethodField()

#     class Meta:
#         model = ProduitVariation
#         fields = '__all__'

#     def get_benefice(self, obj):
#         request = self.context.get('request')
        
#         if request and request.user.is_authenticated:
#             if request.user.role == 'admin':
#                 return obj.benefice()

#         return None

from rest_framework import serializers
from .models import ProduitVariation

class ProduitVariationSerializer(serializers.ModelSerializer):
    benefice = serializers.SerializerMethodField()
    # On ajoute ces lignes pour récupérer les libellés
    nomProduit = serializers.ReadOnlyField(source='produit.nom')
    nomTaille = serializers.ReadOnlyField(source='taille.nom')
    nomCouleur = serializers.ReadOnlyField(source='couleur.nom')
    nomGenre = serializers.ReadOnlyField(source='genre.nom')

    class Meta:
        model = ProduitVariation
        fields = [
            'id', 'produit', 'nomProduit', 'taille', 'nomTaille', 
            'couleur', 'nomCouleur', 'genre', 'nomGenre', 
            'prix_achat', 'prix_vente', 'stock', 'seuil_alerte', 'benefice'
        ]

    def get_benefice(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if request.user.role == 'admin':
                return obj.benefice()
        return None
