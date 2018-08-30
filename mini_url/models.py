from django.db import models
from django.utils import timezone

class MiniURL(models.Model):
    url_longue = models.URLField(max_length=255, unique=True)
    code_raccourci = models.CharField(max_length=20, unique=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de creation")
    pseudo_createur = models.CharField(max_length=50)
    nombre_acces = models.IntegerField(default=0)

    def __str__(self):
        # return self.nom
        return "Mini URL gloglo"
