from django.contrib import admin
from .models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
    # Configuration de la liste de mini-URL
    list_display   = ('url_longue', 'code_raccourci', 'date', 'pseudo_createur', 'nombre_acces', )
    list_filter    = ('pseudo_createur','date', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('url_longue', 'pseudo_createur', )

admin.site.register(MiniURL, MiniURLAdmin)
