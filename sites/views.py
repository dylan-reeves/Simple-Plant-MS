from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from .forms import siteForm
from .models import site
#=========================SITE VIEWS=========================================
# Default landing page for sites app simply displays clickable list of sites


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin']).exists()


class IndexView(generic.ListView):
    template_name = 'sites/index.html'
    context_object_name = 'site_list'

    def get_queryset(self):
        return site.objects.all()

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
# Displays all the fields of a single site entry


class DetailView(generic.DetailView):
    model = site
    template_name = 'sites/details.html'
    context_object_name = 'site_details'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)
# Loads and handles the form to create a new site


class CreateView(generic.CreateView):
    model = site
    template_name = 'sites/create.html'
    fields = ['name', 'manager', 'reportGroup']
    success_url = '/sites/'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

# loads and handles update of sites


class UpdateView(generic.UpdateView):
    model = site
    fields = ['name', 'manager', 'reportGroup']
    template_name = 'sites/update.html'
    success_url = '/sites/'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

# Displays the site delete confirmation page


class DeleteView(generic.DeleteView):
    model = site
    success_url = '/sites/'
    template_name = 'sites/delete.html'
    context_object_name = 'site_details'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)
