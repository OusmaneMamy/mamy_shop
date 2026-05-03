from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from couleurs.models import Couleur
from couleurs.serializers import CouleurSerializer


class CouleurViewSet(ModelViewSet):
    queryset = Couleur.objects.all()
    serializer_class = CouleurSerializer
    permission_classes = [IsAuthenticated]


