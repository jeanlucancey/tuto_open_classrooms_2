from django.contrib import admin
from blog.models import Categorie, Article, Contact

class ArticleAdmin(admin.ModelAdmin):

    # La ligne qui suit est censée remplir le slug avec du Javascript... et
    # ça a fini par marcher, mais pas du premier coup. Pourquoi? Mystère.
    prepopulated_fields = {'slug': ('titre', ), }
    # Autre syntaxe suggérée et que je ne parvenais pas à faire fonctionner:
    # prepopulated_fields = {'slug': ['titre'] }

    # Configuration de la liste d'articles
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'slug', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

    # Colonnes personnalisées 
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut rajouter des points de suspension.
        """
# Tout ce qui suit aurait pu être remplacé par la ligne suivante:
#        return Truncator(article.contenu).chars(40, truncate='...')
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Aperçu du contenu'

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)
