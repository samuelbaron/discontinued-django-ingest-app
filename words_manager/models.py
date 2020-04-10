from django.db import models

class Set(models.Model):
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    set_FK = models.ForeignKey(Set, on_delete=models.CASCADE)

    ''' --- Memobox Legend ---
            0       is not already learning
            1 - 5   is in memobex
            6       words have learned
    '''
    memobox = models.IntegerField(default=1)

    foreign_word = models.CharField(max_length=30)
    native_word = models.CharField(max_length=30)

    native_word_other = models.TextField(blank=True, default='')

    foreign_example = models.TextField(blank=True, default='')
    native_example = models.TextField(blank=True, default='')

    def __str__(self):
        return self.foreign_word


