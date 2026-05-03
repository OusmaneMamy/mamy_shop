from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Achat, LigneAchat
from .serializers import AchatSerializer

class AchatViewSet(viewsets.ModelViewSet):
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.role != 'admin':
            return Response({"error": "Accès refusé"}, status=403)

        lignes_data = request.data.get('lignes', [])
        serializer = self.get_serializer(data=request.data)
        
        # On vérifie la validité et on affiche l'erreur si ça échoue
        if not serializer.is_valid():
            print(f"DEBUG ERREUR ACHAT: {serializer.errors}") # Regarde ton terminal Django !
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                achat = serializer.save()
                for item in lignes_data:
                    LigneAchat.objects.create(
                        achat=achat,
                        variation_id=item.get('variation'), # Utilise l'ID envoyé par Flutter
                        quantite=item.get('quantite'),
                        prix_achat_unitaire=item.get('prix_achat_unitaire')
                    )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
