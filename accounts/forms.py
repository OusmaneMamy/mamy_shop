from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'telephone',
            'adresse',
            'role',
            'password1',
            'password2'
        ]