from django import forms
from .models import MiniURL

class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
#        fields = '__all__'
        fields = ('url_longue', 'pseudo_createur', )

class FromShortcutToUrlForm(forms.ModelForm):
    code_raccourci = forms.CharField(max_length=20, label="Raccourci", required=True)
    # url_longue = forms.URLField(max_length=255)
    # nombre_acces = forms.IntegerField()

    class Meta:
        model = MiniURL
        # fields = '__all__'
        # fields = ('code_raccourci', 'url_longue', 'nombre_acces', )
        fields = ('code_raccourci', )
