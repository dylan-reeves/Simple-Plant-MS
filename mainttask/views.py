from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import MaintenanceJob, MaintenanceTaskDetailItems
# Create your views here.
def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin', 'departmentmanager']).exists()

def is_in_multiple_groups_crud(user):
    return user.groups.filter(name__in=['superadmin', 'siteadmin']).exists()

class IndexView(generic.ListView):
    model = MaintenanceJob
    template_name = 'mainttask/index.html'
    context_object_name = 'mainttask_details'


class DetailView(generic.DetailView):
    model = MaintenanceJob
    template_name = 'mainttask/details.html'
    context_object_name = 'mainttask_details'

class CreateView(generic.CreateView):
    model = MaintenanceJob
    template_name = 'mainttask/create.html'
    fields = ['name','description']
    def dispatch(self, *args, **kwargs):
            self.success_url = '/mainttask/' + self.kwargs['pk']

class UpdateView(generic.UpdateView):
    model = MaintenanceJob
    fields = ['name', 'description']
    template_name = 'mainttask/updtae.html'

    def dispatch(self, *args, **kwargs):
        self.success_url = '/mainttask/' + self.kwargs['pk']

class DeleteView(generic.DeleteView):
    model = MaintenanceJob
    template_name = 'mainttask/delete.html'
    context_object_name = 'maintjob_details'
    success_url = '/maintjobs/'

class AddTaskView(generic.CreateView):
    model = MaintenanceTaskDetailItems
    template_name = 'mainttask/createtask.html'
    fields = ['task']

    def dispatch(self, *args, **kwargs):
        self.model.maintjob = self.kwargs['pk']
        self.success_url = '/mainttask/' + self.kwargs['pk']
