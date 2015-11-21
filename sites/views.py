from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .forms import siteForm

from .models import site
#=========================SITE VIEWS=========================================
# Default landing page for sites app simply displays clickable list of sites


class IndexView(generic.ListView):
    template_name = 'sites/index.html'
    context_object_name = 'site_list'

    def get_queryset(self):
        return site.objects.all()

# Displays all the fields of a single site entry


class DetailView(generic.DetailView):
    model = site
    template_name = 'sites/details.html'
    context_object_name = 'site_details'

# Loads and handles the form to create a new site


class CreateView(generic.CreateView):
    model = site
    template_name = 'sites/create.html'
    fields = ['name', 'manager', 'reportGroup']
    success_url = '/sites/'

# loads and handles update of sites


class UpdateView(generic.UpdateView):
    model = site
    fields = ['name', 'manager', 'reportGroup']
    template_name = 'sites/update.html'
    success_url = '/sites/'

# Displays the site delete confirmation page


class DeleteView(generic.DeleteView):
    model = site
    success_url = '/sites/'
    template_name = 'sites/delete.html'
    context_object_name = 'site_details'
