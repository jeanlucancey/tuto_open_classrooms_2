from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MiniURL
from .forms import MiniURLForm
import random
import string

def accueil(request):
    form = MiniURLForm(request.POST or None)
    if form.is_valid():
        url_longue      = form.cleaned_data['url_longue']
        pseudo_createur = form.cleaned_data['pseudo_createur']
        code_raccourci  = "http://je_suis_accueil." + generer(5)
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
