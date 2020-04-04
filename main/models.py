from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    ''' --------- TO DO -----------
        example in native language 
        example in foreign language
        ---------------------------
    ''' 

    foreign_word = models.CharField(max_length=30)
    native_word = models.CharField(max_length=30)

    def __str__(self):
        return self.foreign_word


