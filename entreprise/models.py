from django.db import models
from autoslug import AutoSlugField
import secrets

TYPE_IMP = (
        ('A4','A4'),
        ('xp','Xprinter'),
)
DEPOT = (
        ('Oui','Oui'),
        ('Non','Non'),
    )
VERSEMENT = (
        ('Oui','Oui'),
        ('Non','Non'),
    )
SMS = (
        ('Oui','Oui'),
        ('Non','Non'),
    )
TYPE_ENTREPRISE = (
        ('commerce general','Commerce general'),
        ('Super marché','Super marché'),
        ('Restaurant','Restaurant'),
        ('Vetement','Vetement'),
        ('Vitrerie','Vitrerie'),
        ('Garage','Garage'),
        ('Clinique','Clinique'),
    )

class Entreprise(models.Model):
    nom=models.CharField(max_length=50,verbose_name="Nom de l'entreprise",null=True,blank=True)
    abreviation=models.CharField(max_length=50,verbose_name="Abreviation",null=True,blank=True)
    logo=models.ImageField(upload_to="logo",verbose_name="logo de l'entreprise",null=True,blank=True)
    email=models.EmailField(max_length=50,verbose_name="Email",null=True,blank=True)
    site=models.CharField(max_length=50,verbose_name="Site Web",null=True,blank=True)
    rccm=models.CharField(max_length=50,verbose_name="RCCM",null=True,blank=True)
    telephone=models.CharField(max_length=50,verbose_name="Téléphone",null=True,blank=True)
    adresse=models.CharField(max_length=50,verbose_name="Adresse",null=True,blank=True)
    # services=RichTextField(null=True,blank=True)
    services=models.TextField(null=True,blank=True)
    type_imprimante=models.CharField(max_length=50,choices=TYPE_IMP)
    type_entreprise=models.CharField(max_length=50,choices=TYPE_ENTREPRISE)
    depot_stock=models.CharField(max_length=50,choices=DEPOT,verbose_name="Avez-vous un dépot de stockage ?")
    initial_recu=models.CharField(max_length=50,verbose_name="Initial Reference Recu",null=True,blank=True)
    initial_facture=models.CharField(max_length=50,verbose_name="Initial Reference Facture",null=True,blank=True)
    initial_devis=models.CharField(max_length=50,verbose_name="Initial Reference Dévis",null=True,blank=True)
    initial_achat=models.CharField(max_length=50,verbose_name="Initial Reference Achat",null=True,blank=True)
    initial_dette=models.CharField(max_length=50,verbose_name="Initial Reference Dette",null=True,blank=True)
    slug = AutoSlugField(unique=True,editable=False)
    cachet=models.ImageField(upload_to="cachet",verbose_name="Cachet et signature",null=True,blank=True)
    dates=models.DateField(auto_now_add=True)
    versements=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous les versements client ?")
    proform=models.TextField(choices=VERSEMENT,verbose_name="Faites-vous des facture proforma ?",default="Oui")
    dettes=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous les dettes ?",default="Oui")
    retours=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous les retours ?",default="Oui")
    sms_vente=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous l'envoie des messages lors d'une vente ?",default="Non")
    sms_versement=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous l'envoie des messages lors d'un versement ?",default="Non")
    sms_reglement=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous l'envoie des messages lors d'un reglement client ?",default="Non")
    sms_reglement_fournisseur=models.TextField(choices=VERSEMENT,verbose_name="Acceptez-vous l'envois des messages lors d'un reglement fournisseur ?",default="Non")
    couleur_entete=models.TextField(verbose_name="Couleur de fond facture",null=True,blank=True,default="#D68F63")
    couleur_text=models.TextField(verbose_name="Couleur du text",null=True,blank=True,default="#000000")
    header_left=models.TextField(verbose_name="header left",null=True,blank=True,default="#28A745")
    header_right=models.TextField(verbose_name="header right",null=True,blank=True,default="#28A745")
    icons=models.TextField(verbose_name="Icons",null=True,blank=True,default="#28A745")
    #----------------------------------------------------SMS----------------------------------------------------------
    username=models.TextField(verbose_name="Username",null=True,blank=True)
    sender=models.TextField(verbose_name="Sender Name",null=True,blank=True)
    token=models.TextField(verbose_name="Token",null=True,blank=True)




    def save(self, *args, **kwargs):
        self.slug = secrets.token_hex(16)
        super().save(*args, **kwargs)
        
    class Meta:
        db_table="entreprise"
        ordering=['-id']
    
    def __str__(self):
        return self.nom
    



