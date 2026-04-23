from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    benefice = serializers.SerializerMethodField()

    class Meta:
        model = Produit
        fields = ['id', 'nom', 'prix_vente', 'stock', 'benefice']

    def get_benefice(self, obj):
        request = self.context.get('request')

        # seul admin voit le bénéfice réel
        if request.user.role == 'admin':
            return obj.prix_vente - obj.prix_achat
        return None