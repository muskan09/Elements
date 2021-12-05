from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutStuff, WorkExp, Education, Language, Domain, Platform
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

def DetailsPageView(request):
    abt = AboutStuff.objects.all()
    exp = WorkExp.objects.all()
    edu = Education.objects.all()
    lang = Language.objects.all()
    dom = Domain.objects.all()
    plat = Platform.objects.all()

    template_name = 'details.html'

    return render(request, template_name, 
                  {
                      'about':abt,
                      'exp':exp,
                      'edu':edu,
                      'lang':lang,
                      'dom':dom,
                      'plat':plat        
                  })
