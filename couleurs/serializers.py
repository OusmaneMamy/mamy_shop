from rest_framework import serializers
from .models import Couleur

class CouleurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couleur
        fields = '__all__'