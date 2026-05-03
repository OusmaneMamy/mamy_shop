from rest_framework import serializers
from .models import Depense

class DepenseSerializer(serializers.ModelSerializer):
    # Pour afficher le texte lisible de la catégorie dans Flutter
    categorie_display = serializers.CharField(source='get_categorie_display', read_only=True)

    class Meta:
        model = Depense
        fields = [
            'id', 'titre', 'categorie', 'categorie_display', 
            'montant', 'date_depense', 'description'
        ]
