from django import forms
from .models import Topic

# Jaki mondry komentaqrz

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'text': ''}