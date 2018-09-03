from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil', views.accueil, name='accueil'),
    path('voir_mini_url', views.voir_mini_url, name='voir_mini_url'),
    path('raccourci_vers_url', views.raccourci_vers_url, name='raccourci_vers_url'),
]
