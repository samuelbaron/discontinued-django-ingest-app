# Functions import
from django.shortcuts import render, redirect
from django.urls import reverse

# Objects import
from .models import *

# Forms import
from .forms import TopicForm


def display_topics(request):
    topics = Topic.objects.order_by('-date_added')
    return render(request, 'words_manager/display_topics.html', {'topics': topics})

# Tata jest super

def add_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('words_manager:display_topics'))

    return render(request, 'words_manager/add_topic.html', {'form': form})