from django.views import generic

from .models import Icecream

class IndexView(generic.ListView):
    template_name = 'icecream/index.html'
    model = Icecream

    def get_context_data(self, **kwargs):
        daily = Icecream.objects.filter(available = 'daily')
        weekly = Icecream.objects.filter(available = 'weekly')
        seasonal = Icecream.objects.filter(available = 'seasonal')
        featured = Icecream.objects.filter(featured = True)

        context = {
            'daily': daily,
            'weekly': weekly,
            'seasonal': seasonal,
            'featured': featured
        }

        return context
    # def get_queryset(self):
    #     filter = models
    #     return Icecream.objects.filter(available = 'weekly')

        # qs = super().get_queryset()
        # # filter by a variable captured from url, for example
        # return qs.filter(name__startswith=self.kwargs['name'])
# Create your views here.
