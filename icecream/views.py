from django.views import generic
from django.urls import reverse_lazy ##reverse_lazy returns you after function is completed (use for delete)
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

## Need CreateView, DetailView, DeleteView, UpdateView
## With template_name and model

##create class for CreateView
