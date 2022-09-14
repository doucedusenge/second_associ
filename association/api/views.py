from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class MembreViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Membre.objects.all()
    serializer_class=MembreSerializer


class CotisationViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Cotisation.objects.all()
    serializer_class=CotisationSerializer


class RemboursementViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Remboursement.objects.all()
    serializer_class=RemboursementSerializer 

class CreditViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Credit.objects.all()
    serializer_class=CreditSerializer

    @action(detail=True, methods=['post'],url_path=r"remboursement", url_name=r"remboursement",serializer_class=Rembourse)
    def rembourse(self,request,pk):
        credit=self.get_object()
        rembourse_obj=Remboursement(
            credit=credit,
            montant=request.data.get("montant")
        )
        rembourse_obj.save() 
        return Response(200)

class CommuniqueViewset(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Communique.objects.all()
    serializer_class=CommuniqueSerializer

        

class ProvinceViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Province.objects.all()
    serializer_class=ProvinceSerializer
  
  

class CommuneViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Commune.objects.all()
    serializer_class=CommuneSerializer

class ZoneViewSet(viewsets.ModelViewSet):
    authentication_classes=[SessionAuthentication]
    permission_classes= [AllowAny]
    queryset=Zone.objects.all()
    serializer_class=ZoneSerializer    
