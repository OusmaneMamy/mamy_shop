from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('assistant', 'Assistant'),
    )

    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='assistant')
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    is_active_account = models.BooleanField(default=True)

    
    class Meta:
        db_table = "accounts"

    def __str__(self):
        return f"{self.username} ({self.role})"

    #permissions simples
    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_assistant(self):
        return self.role == 'assistant'