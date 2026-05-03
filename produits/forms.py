# produits/forms.py

from django import forms
from .models import *

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'


