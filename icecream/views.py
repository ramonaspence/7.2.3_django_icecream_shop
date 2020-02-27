from django.views import generic
from django.urls import reverse_lazy ##reverse_lazy returns you after function is completed (use for delete)
from .models import Icecream

class IndexView(generic.ListView):
    template_name = 'icecream/index.html'
    model = Icecream

    def get_queryset(self):
        if 'selection' in self.kwargs:
            filter = self.kwargs['selection']

            if filter == 'featured':
                return Icecream.objects.filter(featured=True)
            else:
                return Icecream.objects.filter(available=self.kwargs['selection'].lower())
        return Icecream.objects.all()

    ##should not have multiple get_queryset methods

    # def get_context_data(self, **kwargs):
    #     daily = Icecream.objects.filter(available = 'daily')
    #     weekly = Icecream.objects.filter(available = 'weekly')
    #     seasonal = Icecream.objects.filter(available = 'seasonal')
    #     featured = Icecream.objects.filter(featured = True)
    #
    #     context = {
    #         'daily': daily,
    #         'weekly': weekly,
    #         'seasonal': seasonal,
    #         'featured': featured
    #     }
    #
    #     return context

class CreateView(generic.CreateView):
    template_name = 'icecream/add.html'
    model = Icecream
    fields = '__all__'

class DeleteView(generic.DeleteView):
    model = Icecream
    success_url = reverse_lazy('icecream:index')

class UpdateView(generic.UpdateView):
    model = Icecream
    fields = '__all__'
    template_name_suffix = '_update_form'

class DetailView(generic.DetailView):
    model = Icecream
    template_name = 'icecream/detail.html'



## Need CreateView, DetailView, DeleteView, UpdateView
## With template_name and model

##create class for CreateView
