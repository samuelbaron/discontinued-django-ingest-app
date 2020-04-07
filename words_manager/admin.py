from django.contrib import admin

# Register your models here.

from .models import Set, Word

for model in (Set, Word):
    admin.site.register(model)

