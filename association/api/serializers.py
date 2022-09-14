from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.db.models import Sum




class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Membre
        fields="__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["Province"] = ProvinceSerializer(instance.Province,many=False).data
        representation["Commune"] = CommuneSerializer(instance.Commune,many=False).data
        representation["Zone"] = ZoneSerializer(instance.Zone,many=False).data

    
        return representation

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Province
        fields="__all__"

class CommuneSerializer(serializers.ModelSerializer):
     class Meta:
        model=Commune
        fields="__all__"  

class CommuniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Communique
        fields="__all__"        


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zone
        fields="__all__"


class CotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cotisation
        fields="__all__"


    def to_representation(self, instance):
        representation=super().to_representation(instance)
        representation["membre"]=MembreSerializer(instance.membre,many=False).data
        
        return representation 
class Rembourse(serializers.Serializer):
    montant=serializers.IntegerField(required=True) 


class CreditSerializer(serializers.ModelSerializer):
    rembourse=serializers.SerializerMethodField()

    def get_rembourse(self,instance):
        total_rembourse=Remboursement.objects.filter(credit=instance).aggregate(Sum("montant")).get("montant__sum")
        return total_rembourse

    
    class Meta:
        model=Credit
        fields="__all__"



    def to_representation(self, instance):
        reprentation=super().to_representation(instance)
        reprentation["membre"]=MembreSerializer(instance.membre,many=False).data

        return reprentation   

class RemboursementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Remboursement
        fields="__all__"    





        