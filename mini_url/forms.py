from django import forms
from .models import MiniURL

class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
#        fields = '__all__'
        fields = ('url_longue', 'pseudo_createur', )
