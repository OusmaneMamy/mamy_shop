from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'email',
            'telephone',
            'adresse',
            'role',
            'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user