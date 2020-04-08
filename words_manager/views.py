# Functions import
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#from django.http import Http404

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


def set_display(request, set_id):
    '''try:
        spec_set = Set.objects.get(id=set_id)
    except Set.DoesNotExist:
        raise Http404('Erro 404 XDDDD')'''

    spec_set = get_object_or_404(Set, pk=set_id)

    words = spec_set.word_set.all()
    context = {'set': spec_set, 'words': words}
    return render(request, 'words_manager/set_display.html', context)

    