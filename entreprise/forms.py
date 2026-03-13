from django import forms
from .models import Entreprise

class EntrepriseForm(forms.ModelForm):
    class Meta:
      model=Entreprise
      fields='__all__'

      widgets={
			'logo':forms.FileInput(attrs={
				'class':'form-control'
			}),
			'cachet':forms.FileInput(attrs={
				'class':'form-control'
			}),
         	'couleur_entete':forms.TextInput(attrs={
				'type':'color'
			}),
			'couleur_text':forms.TextInput(attrs={
				'type':'color'
			}),

   			'header_left':forms.TextInput(attrs={
				'type':'color'
			}),
   			'header_right':forms.TextInput(attrs={
				'type':'color'
			}),
   			'icons':forms.TextInput(attrs={
				'type':'color'
			}),
      }


class UserEntrepriseForm(forms.ModelForm):
    
    class Meta:
      model=Entreprise
      exclude=['type_entreprise','depot_stock','initial_recu','initial_facture','initial_devis','initial_achat','initial_dette','versements','header_left','header_right','icons','username','sender','token']

      widgets={
			'logo':forms.FileInput(attrs={
				'class':'form-control'
			}),
			'cachet':forms.FileInput(attrs={
				'class':'form-control'
			}),
			'couleur_entete':forms.TextInput(attrs={
				'type':'color'
			}),
			'couleur_text':forms.TextInput(attrs={
				'type':'color'
			}),
   
      }


    
