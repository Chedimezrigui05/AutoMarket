from django.db import models


class Produit(models.Model):
    CATEGORIE_CHOICES = [
        ('berline', 'Berline'),
        ('suv', 'SUV'),
        ('sport', 'Sportive'),
        ('electrique', 'Électrique'),
        ('luxe', 'Luxe'),
        ('crossover', 'Crossover'),
    ]

    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default='berline')
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    en_stock = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    nom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    produit = models.CharField(max_length=200)
    quantite = models.IntegerField(default=1)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.produit}"


class ContactMessage(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"