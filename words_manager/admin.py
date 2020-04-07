from django.contrib import admin

# Register your models here.

from .models import Topic, Word

for model in (Topic, Word):
    admin.site.register(model)

