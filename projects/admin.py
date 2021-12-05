from django.contrib import admin
from .models import Project, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model=Comment
    list_display=('comment', 'author', 'created')
    list_filter=('created')
    search_fields=('comment', 'author')

class ProjectAdmin(admin.ModelAdmin):
    inlines=[
            CommentInline,
        ]
    list_display=('title', 'topics')

admin.site.register(Project, ProjectAdmin);