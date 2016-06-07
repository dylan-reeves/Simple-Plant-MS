from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import MaintenanceJob, MaintenanceTaskDetailItems
from .forms import CopyForm
# Create your views here.
# This method just check to see if the user is a member of the superadmin or
# manager group as these are the only gourps that are allowed to view
# maintenance jobs


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'manager']).exists()

#==============================================================================
#========================GENERIC MAINTENCE JOB VIEW============================
#==============================================================================
# this view displays a list of the setup maintennce jobs


class IndexView(generic.ListView):
    model = MaintenanceJob
    template_name = 'mainttask/index.html'
    context_object_name = 'mainttask_details'

    # check to see if the user is a member of the superadmin or manager groups
    # and dispatch the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

#==============================================================================
#================DETAIL VIEW FOR MAINTENANCE JOB===============================
#==============================================================================
# This view shows the details of a selected maintenance job.


class DetailView(generic.DetailView):
    model = MaintenanceJob
    template_name = 'mainttask/details.html'
    context_object_name = 'mainttask_details'

    # Additional context object to hold all the maintenance tasks for the selected
    # maintenance job
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        prikey = self.kwargs['pk']
        context['task_list'] = MaintenanceTaskDetailItems.objects.filter(
            maintjob=prikey).order_by('orderfield')
        # print(context)
        return context

    # Check to see if the logged on user is a member of superadmin or manager
    # group and dispatch view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

#==============================================================================
#=============CREATE VIEW FOR MAINTENANCE JOBS=================================
#==============================================================================
# This view enables the user to create a maintenance jobs


class CreateView(generic.CreateView):
    model = MaintenanceJob
    template_name = 'mainttask/create.html'
    fields = ['name', 'description']
    success_url = '/maintjobs/'

    # check to see if the user is a member of the superadmin or the managers
    # group and then dispatch the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

#==============================================================================
#=======================VIEW TO UPDATE MAINTENANCE JOBS========================
#==============================================================================
# This view facilitates the modification of existing maintenance jobs


class UpdateView(generic.UpdateView):
    model = MaintenanceJob
    fields = ['name', 'description']
    template_name = 'mainttask/update.html'
    success_url = '/maintjobs/'

    # check to see if the user is a memeber of the superadmin or mamangers group
    # and then dispatch the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

#==============================================================================
#========================VIEW TO DELETE MAINTENANCE JOBS=======================
#==============================================================================
# This view facilitates the deletion of maintenance jobs


class DeleteView(generic.DeleteView):
    model = MaintenanceJob
    template_name = 'mainttask/delete.html'
    context_object_name = 'maintjob_details'
    success_url = '/maintjobs/'
    # check to see if the user is a member of the superadmin or managers group
    # and then dispatch the view

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

#==============================================================================
#======================VIEW TO ADD TASKS TO A JOB==============================
#==============================================================================
# This view is used to add inidividual task items to a maintenance job


class AddTaskView(generic.CreateView):
    model = MaintenanceTaskDetailItems
    template_name = 'mainttask/createtask.html'
    fields = ['task']
    # Check that the user is a member of the superadmin or the amanger group
    # before dispatching the view

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def disptach(self, *args, **kwargs):
        return super(AddTaskView, self).dispatch(*args, **kwargs)

    # handles the form validation and saving
    def form_valid(self, form):
        task = form.save(commit=False)
        # job stores the maintenance job that the task is assigned to
        job = MaintenanceJob.objects.get(pk=self.kwargs['pk'])
        task.maintjob = job
        # The if statement check to see if any other tasks assigned to the
        # maintenance job exist. If they do it incremnts the ordefield. If not
        # the orderfield is set to 1
        if MaintenanceTaskDetailItems.objects.filter(maintjob=self.kwargs['pk']).exists():
            record = MaintenanceTaskDetailItems.objects.filter(
                maintjob=self.kwargs['pk']).latest('orderfield')
            ordernumber = record.orderfield + 1
            task.orderfield = ordernumber
        else:
            task.orderfield = 1
        return super(AddTaskView, self).form_valid(form)
    # the success url is set to addanothertask which asks the user if the want to
    # continue adding tasks to the maintenance job.

    def get_success_url(self):
        return '/maintjobs/' + self.kwargs['pk'] + '/addanothertask/'

#==============================================================================
#====================VIEW ADD ANOTHER TASK=====================================
#==============================================================================
# The view asks if the user wants to add more tasks to the maintenance job or is
# finished adding tasks


class AddAnotherTaskView(generic.DetailView):
    model = MaintenanceJob
    template_name = 'mainttask/addanothertask.html'
    context_object_name = 'mainttask_details'
    # check that the user is a member of the superadmin or the managers group
    # before diaptching the view

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def disptach(self, *args, **kwargs):
        return super(AddAnotherTaskView, self).dispatch(*args, **kwargs)

#==============================================================================
#====================VIEW TO UPDATE A TASK=====================================
#==============================================================================
# The view allows the user to modify a task


class UpdateTaskView(generic.UpdateView):
    model = MaintenanceTaskDetailItems
    template_name = "mainttask/update.html"
    fields = ['orderfield', 'task']
    success_url = '/maintjobs/'
    # check to see that the user is a member of the superadmin or the manager
    # group before dispatching the view

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateTaskView, self).dispatch(*args, **kwargs)

#==============================================================================
#=====================VIEW TO DELETE A TASK====================================
#==============================================================================
# This view allows the user to delete a task from a maintenance job


class DeleteTaskView(generic.DeleteView):
    model = MaintenanceTaskDetailItems
    template_name = 'mainttask/deletetask.html'
    context_object_name = 'maintjob_details'
    success_url = '/maintjobs/'
    # check the user is a member of the superadmin or manager group before
    # dispatching the view

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteTaskView, self).dispatch(*args, **kwargs)

#==============================================================================
#================COPY MAINTENANCE JOB VIEW=====================================
#==============================================================================
# This view will create a copy of an exisitng maintenance job and all the
# associated job tasks. As is visible this is not a Class based view and
# the view is also very badly named.


def CopyView(request, pk):
    # sourcemaintjob refers to the maintenance job object that will be copied
    # This view makes use of the form object call CopyForm
    sourcemaintjob = MaintenanceJob.objects.get(pk=pk)
    if request.method == 'POST':
        form = CopyForm(request.POST)
        if form.is_valid():
            newmaintjob = MaintenanceJob(name=request.POST.get('name'),
                                         description=request.POST.get('description'))
            newmaintjob.save()
            # Once the new job is created the tasks for the source job are
            # retreived from the model and readdedusing the new job
            sourcemainttasks = MaintenanceTaskDetailItems.objects.filter(
                maintjob=sourcemaintjob)
            taskorder = 1
            for task in sourcemainttasks:
                copymainttask = MaintenanceTaskDetailItems(orderfield=taskorder,
                                                           task=task.task, maintjob=newmaintjob)
                copymainttask.save()
                taskorder = taskorder + 1
        return HttpResponseRedirect('/maintjobs/')
    else:
        form = CopyForm()
    return render(request, 'mainttask/copy.html', {'form': form, 'job': sourcemaintjob})
