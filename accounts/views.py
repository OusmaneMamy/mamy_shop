from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status

from .models import Account
from .serializers import AccountSerializer

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'admin'
        )
    
class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     user = self.request.user

    #     if not user.is_authenticated:
    #         return Account.objects.none()

    #     if user.role == 'admin':
    #         return Account.objects.all()

    #     return Account.objects.filter(id=user.id)
    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Account.objects.all()

        return Account.objects.filter(id=user.id)

    def create(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated or user.role != 'admin':
            return Response(
                {"error": "Seul le propriétaire peut créer un compte"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()

        if not user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if user.role == 'admin' or instance.id == user.id:
            return super().update(request, *args, **kwargs)

        return Response(
            {"error": "Accès refusé"},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated or user.role != 'admin':
            return Response(
                {"error": "Suppression interdite"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)