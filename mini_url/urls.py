from django.conf.urls import url
from . import views

# Ce qui suit (avec les expressions regulieres imbitables)
# vient de la correction. Voir plus loin comment faire autrement.

urlpatterns = [
    # Une string vide indique la racine
    url(r'^$', views.liste, name='url_liste'),
    url(r'^nouveau$', views.nouveau, name='url_nouveau'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
]

# Moi (NDJLA), j'avais survecu
# sans expressions regulieres, comme ceci:
# from django.urls import path, re_path
# from . import views
#
# urlpatterns = [
#     path('', views.accueil, name='accueil'),
#     path('accueil', views.accueil, name='accueil'),
#     path('voir_mini_url', views.voir_mini_url, name='voir_mini_url'),
#     path('raccourci_vers_url', views.raccourci_vers_url, name='raccourci_vers_url'),
# ]
