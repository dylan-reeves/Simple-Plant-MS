from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from .models import department
from sites.models import site

#=======================DEPARTMENTS VIEWS======================================
# Default landing page for departments app simply displays a clickable
# list of departments

def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin', 'departmentmanager']).exists()


class IndexView(generic.ListView):
    model = department
    template_name = 'departments/index.html'
    context_object_name = 'department_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['all_sites'] = site.objects.values_list('name', flat=True)
        return context

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

# Displays all the fields of a single department entry


class DetailView(generic.DetailView):
    model = department
    template_name = 'departments/details.html'
    context_object_name = 'department_details'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

# Loads and handles the form to create a new department


class CreateView(generic.CreateView):
    model = department
    template_name = 'departments/create.html'
    fields = ['name', 'manager', 'sites']
    success_url = '/departments/'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

# Loads and handles the departments update


class UpdateView(generic.UpdateView):
    model = department
    fields = ['name', 'manager', 'sites']
    template_name = 'departments/update.html'
    success_url = '/departments/'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

# Displays the department delete confirmation page


class DeleteView(generic.DeleteView):
    model = department
    success_url = '/departments/'
    template_name = 'departments/delete.html'
    context_object_name = 'department_details'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)
