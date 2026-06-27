from django.contrib import admin
from .models import Produit, Commande, ContactMessage

admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(ContactMessage)
