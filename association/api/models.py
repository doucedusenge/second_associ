import datetime
import email
from email import message
from msilib.schema import Class
from pickle import FALSE, TRUE
from turtle import mode
from django.db import models

# Create your models here.


class Province(models.Model):
    id=models.AutoField(primary_key=True)
    nom_province=models.CharField(max_length=50)  
    
    def __str__(self) -> str:
        return self.nom_province

class Commune(models.Model):
    id=models.AutoField(primary_key=True)
    nom_commune=models.CharField(max_length=50)
    province=models.ForeignKey(Province,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.nom_commune
        

class Zone(models.Model):
    id=models.AutoField(primary_key=True)
    nom_Zone=models.CharField(max_length=50) 
    commune=models.ForeignKey(Commune,on_delete=models.CASCADE,null=True)   

    def __str__(self) -> str:
        return  self.nom_Zone
    
        
class Membre(models.Model):
    GENRE=(('Masculin','Masculin'),('Féminin','Féminin'))
    ETAT=(('Célibataire','Célibataire'),('Marié','Marié'))
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    age=models.PositiveIntegerField(default=0)
    genre=models.CharField(max_length=50, choices=GENRE, null=True)
    etat_civil=models.CharField(max_length=50,choices=ETAT,null=True)
    CNI=models.IntegerField(default=0,null=True)
    contact=models.IntegerField(default=0,null=True)
    email=models.EmailField(null=True)
    Province=models.ForeignKey(Province,on_delete=models.CASCADE)
    Commune=models.ForeignKey(Commune,on_delete=models.CASCADE)
    Zone=models.ForeignKey(Zone,on_delete=models.CASCADE)
    residence_actuelle=models.CharField(max_length=50)
    photo=models.ImageField(null=True)
   
    def __str__(self) -> str:
        return self.nom       

            
class Communique(models.Model):
    id=models.BigAutoField(primary_key=True)
    message=models.TextField(null=True)
    membre=models.ForeignKey(Membre,on_delete=models.CASCADE,null=True) 
    date=models.DateField(auto_now=True,editable=False)        

class Cotisation(models.Model):
    id=models.AutoField(primary_key=True)
    membre=models.ForeignKey(Membre,on_delete=models.CASCADE)  
    montant=models.PositiveIntegerField(default=0)       
    date=models.DateField(auto_now=True,editable=False)

class Credit(models.Model):
    id=models.AutoField(primary_key=True)
    membre=models.ForeignKey(Membre,on_delete=models.CASCADE)  
    motif=models.CharField(max_length=50)
    montant=models.PositiveIntegerField(default=0)
    date=models.DateField(auto_now=True,editable=False)

    

class Remboursement(models.Model):
    id=models.AutoField(primary_key=True)
    credit=models.ForeignKey(Credit,on_delete=models.CASCADE,null=True)
    montant=models.PositiveIntegerField(default=0)
    date=models.DateField(auto_now=True,editable=False)

    def __str__(self) -> str:
        return self.credit


class Adresse(models.Model):
    id=models.AutoField (primary_key=True)
    Membre=models.ForeignKey(Membre,on_delete=models.CASCADE)
    Province=models.ForeignKey(Province,on_delete=models.CASCADE)
    Commune=models.ForeignKey(Commune,on_delete=models.CASCADE)
    Zone=models.ForeignKey(Zone,on_delete=models.CASCADE)

       
   







