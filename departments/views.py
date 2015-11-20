from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from .models import department
from sites.models import site

#=======================DEPARTMENTS VIEWS======================================
#Default landing page for departments app simply displays a clickable list of departments
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

#Displays all the fields of a single department entry
class DetailView(generic.DetailView):
    model = department
    template_name = 'departments/details.html'
    context_object_name = 'department_details'

#Loads and handles the form to create a new department
class CreateView(generic.CreateView):
    model = department
    template_name = 'departments/create.html'
    fields = ['name', 'manager', 'reportGroup']
    success_url = '/departments/'

#Loads and handles the departments update
class UpdateView(generic.UpdateView):
    model = department
    fields = ['name', 'manager', 'reportGroup']
    template_name = 'departments/update.html'
    success_url = '/departments/'

#Displays the department delete confirmation page
class DeleteView(generic.DeleteView):
    model = department
    success_url = '/departments/'
    template_name = 'departments/delete.html'
    context_object_name = 'department_details'
