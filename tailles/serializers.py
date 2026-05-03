from rest_framework import serializers
from .models import Taille

class TailleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taille
        fields = '__all__'