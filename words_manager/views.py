# Functions import
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
#from django.http import Http404

# Objects import
from .models import *

# Forms import
from .forms import SetForm, WordForm


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


def set_edit(request, set_id):

    spec_set = get_object_or_404(Set, pk=set_id)

    words = spec_set.word_set.all()
    context = {'set': spec_set, 'words': words}
    return render(request, 'words_manager/set_edit.html', context)


def word_add(request, set_id):
    spec_set = get_object_or_404(Set, pk=set_id)

    if request.method != 'POST':
        form = WordForm()
    else:
        form = WordForm(request.POST)
        if form.is_valid():
            new_words = form.save(commit=False)
            new_words.set_FK = spec_set
            new_words.save()
            return redirect(reverse('words_manager:set_edit', args=[set_id]))

    context = {
        'form': form,
        'set': spec_set,
    }

    return render(request, 'words_manager/word_add.html', context)


def word_edit(request, word_id):
    spec_word = get_object_or_404(Word, pk=word_id)
    spec_set = spec_word.set_FK

    if request.method != 'POST':
        form = WordForm(instance=spec_word)
    else:
        form = WordForm(request.POST, instance=spec_word)
        if form.is_valid():
            form.save()
            return redirect(reverse('words_manager:set_edit', args=[spec_set.id]))

    context = {
        'form': form,
        'word': spec_word,
    }

    return render(request, 'words_manager/word_edit.html', context)


def set_delete(request, set_id):
    spec_set = Set.objects.get(id=set_id)
    spec_set.delete()
    return redirect(reverse('words_manager:sets_display'))


def word_delete(request, word_id):
    spec_word = Word.objects.get(id=word_id)
    spec_set = spec_word.set_FK
    spec_word.delete()
    return redirect(reverse('words_manager:set_display', args=[spec_set.id]))
    