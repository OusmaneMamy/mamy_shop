from django import forms
from .models import *


class ProduitVariationForm(forms.ModelForm):
    class Meta:
        model = ProduitVariation
        fields = '__all__'