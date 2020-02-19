from django.views import generic

class BaseView(generic.TemplateView):
    template_name = '.base.html'

class IndexView(generic.TemplateView):
    template_name = 'icecream/index.html'





# Create your views here.
