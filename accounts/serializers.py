from rest_framework import serializers
from accounts.models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = Utilisateur
        fields = [
            "id",
            "username",
            "nom",
            "prenom",
            "email",
            "telephone",
            "statut",
            "roles",
        ]

    def get_roles(self, obj):
        """
        Retourne une liste des noms de groupes (rôles) de l'utilisateur
        """
        return [group.name for group in obj.groups.all()]