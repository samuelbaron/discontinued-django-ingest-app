# Functions import
from django.shortcuts import render, redirect
from django.urls import reverse

# Objects import
from .models import *

# Forms import
from .forms import SetForm


def sets_display(request):
    sets = Set.objects.order_by('-date_added')
    return render(request, 'words_manager/sets_display.html', {'sets': sets})


def set_add(request):
    if request.method != 'POST':
        form = SetForm()
    else:
        form = SetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('words_manager:sets_display'))

    return render(request, 'words_manager/set_add.html', {'form': form})