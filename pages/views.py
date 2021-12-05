from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutStuff, WorkExp, Education, Languages, Domains, Platforms
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

def DetailsPageView(request):
    abt = AboutStuff.objects.all()
    exp = WorkExp.objects.all()
    edu = Education.objects.all()
    lang = Languages.objects.all()
    dom = Domains.objects.all()
    plat = Platforms.objects.all()

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
