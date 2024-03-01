from django import forms
from .models import CharacterSheet

class CharacterSheetForm(forms.ModelForm):
    class Meta:
        model = CharacterSheet
        fields = ['character_name', 'character_class']