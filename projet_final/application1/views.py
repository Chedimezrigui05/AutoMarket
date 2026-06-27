from django.shortcuts import render
from .models import Produit, Commande, ContactMessage


def accueil(request):
    return render(request, 'application1/accueil.html')


def about(request):
    return render(request, 'application1/about.html')


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            sujet=request.POST.get('sujet'),
            message=request.POST.get('message')
        )
        return render(request, 'application1/contact.html', {'success': True})
    return render(request, 'application1/contact.html')


def catalogue(request):
    tous_produits = Produit.objects.filter(en_stock=True)

    produits = {
        'berline': tous_produits.filter(categorie='berline'),
        'suv': tous_produits.filter(categorie='suv'),
        'sport': tous_produits.filter(categorie='sport'),
        'electrique': tous_produits.filter(categorie='electrique'),
        'luxe': tous_produits.filter(categorie='luxe'),
        'crossover': tous_produits.filter(categorie='crossover'),
    }

    return render(request, 'application1/catalogue.html', {'produits': produits})


def commander(request):
    produits = Produit.objects.filter(en_stock=True)
    
    if request.method == 'POST':
        Commande.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            adresse=request.POST.get('adresse'),
            produit=request.POST.get('produit'),
            quantite=request.POST.get('quantite', 1)
        )
        return render(request, 'application1/commander.html', {'success': True, 'produits': produits})
    return render(request, 'application1/commander.html', {'produits': produits})