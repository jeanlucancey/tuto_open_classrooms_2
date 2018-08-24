from django.urls import path, re_path
from . import views

# urlpatterns = [
#     re_path(r'^accueil', views.home),
#     re_path(r'^article/(?P<id_article>.+)', views.view_article), 
#     re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),  
#     path('articles/<int:year>/<int:month>', views.list_articles),  
#     re_path(r'^articles/(?P<tag>.+)', views.list_articles_by_tag), 
#     path('redirection', views.view_redirection),
#     path('article/<int:id_article>$', views.view_article, name='afficher_article'),
# ]

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('article2/<int:id>-<slug:slug>', views.lire2, name='lire2'),
    path('date', views.date_actuelle),
    path('mapage', views.ma_page),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('proust', views.cree_proust),
]
