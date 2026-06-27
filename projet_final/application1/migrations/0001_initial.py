from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('categorie', models.CharField(choices=[('musculation', 'Musculation'), ('cardio', 'Cardio'), ('nutrition', 'Nutrition'), ('vetements', 'Vêtements'), ('accessoires', 'Accessoires')], default='musculation', max_length=20)),
                ('en_stock', models.BooleanField(default=True)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.TextField()),
                ('produit', models.CharField(max_length=200)),
                ('quantite', models.IntegerField(default=1)),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('confirmee', 'Confirmée'), ('expediee', 'Expédiée'), ('livree', 'Livrée'), ('annulee', 'Annulée')], default='en_attente', max_length=20)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('lu', models.BooleanField(default=False)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
