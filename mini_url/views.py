from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MiniURL
from .forms import MiniURLForm, FromShortcutToUrlForm
import random
import string

def accueil(request):
    form = MiniURLForm(request.POST or None)
    if form.is_valid():
        url_longue      = form.cleaned_data['url_longue']
        pseudo_createur = form.cleaned_data['pseudo_createur']
        # code_raccourci  = "http://jla.ly/" + generer(5)
        code_raccourci  = generer(5)
        date            = timezone.now()
        nombre_acces    = 0

        monUrl = MiniURL()
        monUrl.url_longue = url_longue
        monUrl.pseudo_createur = pseudo_createur
        monUrl.code_raccourci = code_raccourci
        monUrl.date = date
        monUrl.nombre_acces = nombre_acces
        monUrl.save()

        envoi = True
    resultat = render(request, 'mini_url/accueil.html', locals())

    return resultat

def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

    return ''.join(aleatoire)

def voir_mini_url(request):
    mes_mini_url = MiniURL.objects.all() # Nous sélectionnons tous nos articles
    tabMiniUrl = []
    for e in mes_mini_url:
        tabMiniUrl.append(e)
    # mes_mini_url est un QuerySet, tabMiniUrl est un bête tableau
    # sur lequel je peux faire un tri à bulles à la con... ce qui est
    # sûrement une mauvaise idée, mais c'est la seule que j'aie
    nbElts = len(tabMiniUrl)
    for numElt1 in range(len(tabMiniUrl) - 1):
        for numElt2 in range(numElt1, len(tabMiniUrl)):
            accesElt1 = tabMiniUrl[numElt1].nombre_acces
            accesElt2 = tabMiniUrl[numElt2].nombre_acces
            if accesElt2 > accesElt1:
                intermed = tabMiniUrl[numElt1]
                tabMiniUrl[numElt1] = tabMiniUrl[numElt2]
                tabMiniUrl[numElt2] = intermed
    return render(request, 'mini_url/voir_mini_url.html', {'mes_mini_url': tabMiniUrl})

def raccourci_vers_url(request):
    form = FromShortcutToUrlForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        code_raccourci = form.cleaned_data['code_raccourci']
        # url_longue = form.cleaned_data['url_longue']
        # nombre_acces = form.cleaned_data['nombre_acces']
        envoi = True
    return render(request, 'mini_url/raccourci_vers_url.html', locals())
