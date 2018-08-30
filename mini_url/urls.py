from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accuse_reception', views.accuse_reception, name='accuse_reception'),
]
