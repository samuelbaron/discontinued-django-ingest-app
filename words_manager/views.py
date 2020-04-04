from django.shortcuts import render

# Create your views here.
from .models import *

def display_topics(request):
    topics = Topic.objects.order_by('-date_added')
    return render(request, 'words_manager/display_topics.html', {'topics': topics})

def add_topic(request):
    pass