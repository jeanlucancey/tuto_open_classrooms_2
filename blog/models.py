from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42, verbose_name="Nom de l'auteur")
    slug = models.SlugField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    # Ce qui suit est une variante
    # date = models.DateTimeField(auto_now_add=True, auto_now=False, 
    #                             verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, \
                                  verbose_name="Catégorie")
    
    class Meta:
        verbose_name = "article" # Mention employée dans l'interface d'admin
        ordering = ['date']
    
    def __str__(self):
        return self.titre

class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre', 
                                      related_name='+')
    produits_sans_prix = models.ManyToManyField(Produit, related_name="vendeurs")

    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")
    
    def __str__(self):
           return self.nom
