# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import Group
from accounts.models import Utilisateur
from accounts.serializers import UtilisateurSerializer



class ListeUtilisateursAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = Utilisateur.objects.all()
        serializer = UtilisateurSerializer(users, many=True)
        return Response(serializer.data)


class DetailUtilisateurAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if not user:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UtilisateurSerializer(user)
        return Response(serializer.data)


class CreateUtilisateurAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Ajouter les rôles (groupes) si fournis
            roles = request.data.get("roles", [])
            for r in roles:
                try:
                    group = Group.objects.get(name=r)
                    user.groups.add(group)
                except Group.DoesNotExist:
                    continue
            return Response(UtilisateurSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUtilisateurAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
        except Utilisateur.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UtilisateurSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            # Mettre à jour les rôles si fournis
            if "roles" in request.data:
                user.groups.clear()
                for r in request.data["roles"]:
                    try:
                        group = Group.objects.get(name=r)
                        user.groups.add(group)
                    except Group.DoesNotExist:
                        continue
            return Response(UtilisateurSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUtilisateurAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
            user.delete()
            return Response({"message": "Utilisateur supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
        except Utilisateur.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)


class ToggleActiveUtilisateurAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, pk):
        try:
            user = Utilisateur.objects.get(pk=pk)
            user.is_active = not user.is_active
            user.save()
            return Response({"id": user.id, "is_active": user.is_active})
        except Utilisateur.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)