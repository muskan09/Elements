from django.contrib import admin
from .models import AboutStuff, WorkExp, Education, Language, Domain, Platform
# Register your models here.

models = [AboutStuff, WorkExp, Education, Language, Domain, Platform]
admin.site.register(models)