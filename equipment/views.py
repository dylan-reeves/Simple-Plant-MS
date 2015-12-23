from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import equipment



def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin', 'departmentmanager']).exists()


def is_in_multiple_groups_crud(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin']).exists()

# Create your views here.
#=========================EQUIPMENT VIEWS=====================================
class IndexView(generic.ListView):
    model = equipment
    template_name = 'equipment/index.html'
    context_object_name = 'equipment_details'
    #def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['all_sites'] = site.objects.values_list('name', flat=True)
        #return context

#Displays all the fields of a single department entry
class DetailView(generic.DetailView):
    model = equipment
    template_name = 'equipment/details.html'
    context_object_name = 'equipment_details'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        prikey =

#Loads and handles the form to create a new department
class CreateView(generic.CreateView):
    model = equipment
    template_name = 'equipment/create.html'
    fields = ['name', 'code', 'site', 'department', 'nextmaintenancedate', 'intervalType', 'active']
    success_url = '/equipment/'

    @method_decorator(user_passes_test(is_in_multiple_groups_crud, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)
#Loads and handles the departments update
class UpdateView(generic.UpdateView):
    model = equipment
    fields = ['name', 'code', 'site', 'department', 'nextmaintenancedate', 'intervalType', 'active']
    template_name = 'equipment/update.html'
    success_url = '/equipment/'

#Displays the department delete confirmation page
class DeleteView(generic.DeleteView):
    model = equipment
    success_url = '/equipment/'
    template_name = 'equipment/delete.html'
    context_object_name = 'equipment_details'
