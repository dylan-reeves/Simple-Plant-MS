from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse. reverse_lazy
from django.views import generic
from .models import department

#Default landing page for departments app simply displays a clickable list of departments
class IndexView(generic.ListView):
    template_name = 'departments/index.html'
    context_object_name = 'department_list'
    def get_queryset(self):
        return site.objects.all()

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

#TODO Complete Update Form
def index(request):
    return #To Complete

#Displays the department delete confirmation page
class DeleteView(generic.DeleteView):
    model = department
    success_url = reverse_lazy('IndexView')
    template_name = 'departments/delete.html'
    context_object_name = 'department_details'
