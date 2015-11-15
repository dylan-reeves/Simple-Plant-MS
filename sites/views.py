from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from .forms import siteForm

from .models import site

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sites/index.html'
    context_object_name = 'site_list'
    def get_queryset(self):
        return site.objects.all()

class DetailView(generic.DetailView):
    model = site
    template_name = 'sites/details.html'
    context_object_name = 'site_details'

class CreateView(generic.CreateView):
    model = site
    template_name = 'sites/create.html'
    fields = ['name', 'manager', 'reportGroup']
    success_url = '/sites/'

def update(request):
    return render("Update Page")

class DeleteView(generic.DeleteView):
    model = site
    success_url = reverse_lazy('IndexView')
    template_name = 'sites/delete.html'
    context_object_name = 'site_details'
