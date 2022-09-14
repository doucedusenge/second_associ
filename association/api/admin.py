from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Membre)
admin.site.register(Province)
admin.site.register(Commune)
admin.site.register(Zone)
admin.site.register(Cotisation)
admin.site.register(Remboursement)
admin.site.register(Communique)