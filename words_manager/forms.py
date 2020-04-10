from django import forms
from .models import Set, Word


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['name']
        labels = {'text': ''}

    
class WordForm(forms.ModelForm):
    class Meta: 
        model = Word

        fields = [
            # NOT NULL
            'foreign_word',
            'native_word',

            # CAN BE NULL
            'native_word_other',
            'foreign_example',
            'native_example',
        ]

        labels = {
            'foreign_word': '',
            'native_word': '',
            'native_word_other': '',
            'foreign_example': '',
            'native_example': '',
        }