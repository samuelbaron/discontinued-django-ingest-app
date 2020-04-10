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
            'foreign_word': 'Word in foreign language',
            'native_word': 'Word in native language',
            'native_word_other': 'Other meaning (native)',
            'foreign_example': 'Example foreign',
            'native_example': 'Example native',
        }

        widgets = {
            'foreign_word': forms.Textarea(attrs={
                #'class': ''
                'cols': 30,
                'rows': 1,
            }),

            'native_word': forms.Textarea(attrs={
                #'class': ''
                'cols': 30,
                'rows': 1,
            }),

            'native_word_other': forms.Textarea(attrs={
                #'class': '',
                'cols': 30,
                'rows': 2,
                'placeholder': 'optional',
            }),

            'foreign_example': forms.Textarea(attrs={
                #'class': '',
                'cols': 40,
                'rows': 4,
                'placeholder': 'optional',
            }),

            'native_example': forms.Textarea(attrs={
                #'class': '',
                'cols': 40,
                'rows': 4,
                'placeholder': 'optional',
            }),
        }