from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Depense
from .serializers import DepenseSerializer

class DepenseViewSet(viewsets.ModelViewSet):
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # On peut ajouter ici une logique si besoin
        serializer.save()
