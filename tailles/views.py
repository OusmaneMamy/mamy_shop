from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tailles.models import Taille
from tailles.serializers import TailleSerializer


class TailleViewSet(ModelViewSet):
    queryset = Taille.objects.all()
    serializer_class = TailleSerializer
    permission_classes = [IsAuthenticated]