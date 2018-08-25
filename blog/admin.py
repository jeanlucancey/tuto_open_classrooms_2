from django.contrib import admin
from django.utils.text import Truncator

from blog.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('titre', 'contenu')

    # Ce qui suit (facultatif) concerne la présentation du formulaire
    fields = ('date', 'titre', 'auteur', 'categorie', 'contenu')
    
    def apercu_contenu(self, article):
        """ 
        Permet un traitement du champ au lieu de l'afficher brut de fonderie.
        En l'occurrence, retourne les premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(article.contenu).chars(15, truncate='...')
        # return '{' + Truncator(article.contenu).chars(15, truncate='...') + '}'

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
