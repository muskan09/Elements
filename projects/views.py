from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Comment
from .forms import CommentForm
from django.db.models import Q

from environs import Env

env=Env()
env.read_env()

# Create your views here.
class ProjectListView(ListView):
    model=Project
    context_object_name='project_list'
    template_name='projects/project_list.html'


def ProjectDetailView(request, uuid):
    template_name = 'projects/project_detail.html'
    project = get_object_or_404(Project, id=uuid)
    comments = project.comments.all()

    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.project = project
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'project': project, 
                                           'comments': comments,
                                          'comment_form': comment_form
                                           })


class SearchResultsListView(ListView):
    model=Project
    context_object_name='project_list'
    template_name='projects/search_results.html'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Project.objects.filter(
            Q(title__icontains=query)|
            Q(topics__icontains=query)
            ) 