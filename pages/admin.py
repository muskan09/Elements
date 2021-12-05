from django.contrib import admin
from .models import AboutStuff, WorkExp, Education, Languages, Domains, Platforms
# Register your models here.

models = [AboutStuff, WorkExp, Education, Languages, Domains, Platforms]
admin.site.register(models)