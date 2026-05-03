from django.db import models

# Create your models here.
class Genre(models.Model):
    nom = models.CharField(max_length=20) 
    

    class Meta:
        db_table = "genres"
    
    def __str__(self):
        return self.nom