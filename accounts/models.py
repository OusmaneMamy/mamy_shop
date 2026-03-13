from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=100, blank=False, null=True)
    prenom = models.CharField(max_length=100, blank=False, null=True)
    telephone = models.CharField(blank=True, null=True, unique=True, max_length=255)
    statut = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return self.username

    def get_roles_display(self):
        return [group.name for group in self.groups.all()]