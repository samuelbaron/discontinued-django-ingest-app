from django import forms
from .models import Set, Word


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['name']
        labels = {'text': ''}
        widgets = {'name': forms.TextInput(attrs={'id':'form_name'})}
        


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

        widgets = {
            'foreign_word': forms.Textarea(attrs={
                'class': 'add_word_input required',
                'cols': 30,
                'rows': 1,
                'placeholder': 'foreign word',
            }),

            'native_word': forms.Textarea(attrs={
                'class': 'add_word_input required',
                'cols': 30,
                'rows': 1,
                'placeholder': 'native word',
            }),

            'native_word_other': forms.Textarea(attrs={
                'class': 'add_word_input optional',
                'cols': 30,
                'rows': 1,
                'placeholder': 'optional native word',
            }),

            'foreign_example': forms.Textarea(attrs={
                'class': 'add_word_input space optional',
                'cols': 40,
                'rows': 1,
                'placeholder': 'foreign example sentence',
            }),

            'native_example': forms.Textarea(attrs={
                'class': 'add_word_input optional',
                'cols': 40,
                'rows': 1,
                'placeholder': 'meaning',
            }),
        }