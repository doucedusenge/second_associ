from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *

router= routers.DefaultRouter()
router.register("membre",MembreViewSet)
router.register("cotisation",CotisationViewSet)
router.register("credit",CreditViewSet)
router.register("remboursement",RemboursementViewSet)
router.register("province",ProvinceViewSet)
router.register("commune",CommuneViewSet)
router.register("zone",ZoneViewSet)
router.register("communique",CommuniqueViewset)



urlpatterns = [
    path('', include(router.urls)),
    path('api_auth', include('rest_framework.urls'))
    
]