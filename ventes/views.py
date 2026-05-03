from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Vente, LigneVente
from .serializers import VenteSerializer

class VenteViewSet(ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != 'admin':
            return Response({"error": "Accès refusé"}, status=status.HTTP_403_FORBIDDEN)

        lignes_data = request.data.get('lignes', [])
        
        # On valide d'abord l'entête de la vente (montant, mode paiement, etc.)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            # Si erreur 400, Flutter affichera exactement quel champ pose problème
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # Enregistre la Vente
                vente = serializer.save()

                # Enregistre les Lignes
                for item in lignes_data:
                    LigneVente.objects.create(
                        vente=vente,
                        variation_id=item.get('variation'), # Crucial: utilise l'ID
                        quantite=item.get('quantite'),
                        prix_unitaire=item.get('prix_unitaire')
                    )
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
