from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import random
import string

def accueil(request):
    return render(request, 'mini_url/accueil.html', locals())

def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    
    return ''.join(aleatoire)
