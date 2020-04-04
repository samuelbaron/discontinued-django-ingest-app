from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    pass

def user_panel(request):
    pass

def learn(request):
    topics = Topic.objects.order_by('-date_added')
    return render(request, 'main/learn.html', {'topics': topics})