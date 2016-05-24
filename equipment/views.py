from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

from .models import equipment, maintenanceschedule
from maintenance.models import maintenancerecord, maintenancerecorddetails

#========================EQUIPMENT VIEWS=======================================
# Views that handle all the actions to do with the equipment in the system

# The below method is to check that the user is a member of the superadmin or the
# manager group in order to be able to add/update/remove equipment, does not
# require a separate method for CRUD and both groups can perform all actions


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'manager']).exists()

#=============================================================================
#=========================GENERIC EQUIPMENT LIST VIEW=========================
#=============================================================================
# This view is the default landing page for the equipment view and will display
# all equipment for the users department


class IndexView(generic.ListView):
    model = equipment
    template_name = 'equipment/index.html'
    context_object_name = 'equipment_details'

    # Check to see if the user is logged in as superadmin or manager
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    def dispatch(self, request, *args, **kwargs):
        # populate the queryset from the equipment model and filter the response
        # according to the department membership of the user

        # get the departments the user is a member of
        UserDepartments = request.user.usermain.departments.all()
        # Assign the variable to hold the context object which will be created by
        # the Q function
        byDepartmentQuery = Q()
        # Now loop through all the users departments and get the equipment
        # assigned to that department and add it to the query object
        for Department in UserDepartments:
            byDepartmentQuery = byDepartmentQuery | Q(department=Department)
        # populate the queryset according to the Department Query
        self.queryset = equipment.objects.filter(byDepartmentQuery)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

#==============================================================================
#====================EQUIPMENT DETAILS VIEW====================================
#==============================================================================

# Displays all the fields of a single peice of equipment


class DetailView(generic.DetailView):
    model = equipment
    template_name = 'equipment/details.html'
    context_object_name = 'equipment_details'

    # The get_context_data method adds an additional context data library that
    # contains all the scheduled maintenance jobs assigned to the selected peice
    # of equipment
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        prikey = self.kwargs['pk']
        context['schedule_list'] = maintenanceschedule.objects.filter(
            equipment=prikey)
        return context

    # Check to see if the user is logged in as a superadmin or a manager
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    # dispatch the view to the client
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

#==============================================================================
#=======================CREATE EQUIPMENT VIEW==================================
#==============================================================================

# Loads and handles the form to create a new equipment entry


class CreateView(generic.CreateView):
    model = equipment
    template_name = 'equipment/create.html'
    fields = ['name', 'code', 'site', 'department',  'active']
    success_url = '/equipment/'

    # CHecks to ensure user is a member of superadmin or manager group before
    # dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

#==============================================================================
#=======================UPDATE EQUIPMENT VIEW==================================
#==============================================================================

# Loads and handles the equipment update


class UpdateView(generic.UpdateView):
    model = equipment
    fields = ['name', 'code', 'site', 'department',  'active']
    template_name = 'equipment/update.html'
    success_url = '/equipment/'

    # Check user is a member of superadmin or manager group before diaptching the
    # view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

#==============================================================================
#=====================EQUIPMENT DELETE VIEW====================================
#==============================================================================

# Displays the equipment delete confirmation page


class DeleteView(generic.DeleteView):
    model = equipment
    success_url = '/equipment/'
    template_name = 'equipment/delete.html'
    context_object_name = 'equipment_details'

    # Check the user is a memeber of the superadmin or manager groups before
    # dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

#==============================================================================
#=========ADD MAINTENANCE JOB TO EQUIPMENT=====================================
#==============================================================================
# This view links a peice of equipment to a defined maintenance job and defines
# the schedule interval (i.e. every 60 days)


class AddScheduleView(generic.CreateView):
    model = maintenanceschedule
    template_name = 'equipment/addschedule.html'
    fields = ['maintenancejob', 'interval', 'nextdate']
    success_url = '/equipment/'

    # method to handle the form
    def form_valid(self, form):
        schedule = form.save(commit=False)
        # the equip variable is used to store the primary key of the peice of
        # equipment, this is retrieved from the url call. The primary get
        # is required to create the linkage record
        equip = equipment.objects.get(pk=self.kwargs['pk'])
        schedule.equipment = equip
        return super(AddScheduleView, self).form_valid(form)

    # Check that the user is a member of superadmin or manager group before
    # sending the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    def dispatch(self, *args, **kwargs):
        return super(AddScheduleView, self).dispatch(*args, **kwargs)

#==============================================================================
#==================UPDATE MAINTENANCE JOB SCHEDULED TO EQUIPMENT===============
#==============================================================================
# This view would edit the linkage of a peice of equipment to a maintenance job
# This would basically entail changed the maintenance interval


class UpdateScheduleView(generic.UpdateView):
    model = maintenanceschedule
    template_name = 'equipment/update.html'
    fields = ['maintenancejob', 'interval']
    success_url = '/equipment/'

    # Check to see that the user is a member of the superadmin or the managers
    # group before dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateScheduleView, self).dispatch(*args, **kwargs)

#==============================================================================
#===================DELETE THE LINKAGE BETWEEN EQUIP AND MAINTENANCE JOB=======
#==============================================================================
# This view will remove the realtionship between a peice of equipment and a
# defined maintenance job


class DeleteScheduleView(generic.DeleteView):
    model = maintenanceschedule
    template_name = 'equipment/deleteschedule.html'
    context_object_name = 'schedule_details'
    success_url = '/equipment/'

    # check that the user is a member of the superadmin or the manager group
    # before dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteScheduleView, self).dispatch(*args, **kwargs)

#==============================================================================
#=============HISTORY LIST FOR EQUIPMENT VIEW==================================
#==============================================================================
# This view returns all the maintenance tasks conducted for the peice of
# equipment as a list


class MaintHistory(generic.ListView):
    template_name = 'equipment/mainthistory.html'
    context_object_name = 'mainthistory'

    # Check to see if the user is a member of superadmin or manager group before
    # dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        # the below code filters the maintenance records with the equipment
        # primary key from the url as a filter
        self.queryset = maintenancerecord.objects.filter(
            equipment=self.kwargs['pk'])
        return super(MaintHistory, self).dispatch(*args, **kwargs)

#==============================================================================
#========MAINTENANCE HISTORY DETAILS===========================================
#==============================================================================
# This view shows the details for an individual completed maintenance job


class HistoryDetails(generic.DetailView):
    template_name = 'equipment/mainthistorydetails.html'
    context_object_name = 'mainthistory'

    # Below creates an additional context object that is populated with the
    # inidividual tasks of the maintenance job
    def get_context_data(self, **kwargs):
        context = super(HistoryDetails, self).get_context_data(**kwargs)
        context['mainthistorydetails'] = maintenancerecorddetails.objects.filter(
            maintenancerecord=self.kwargs['pk'])
        return context

    # Check the user is a member of superadmin or managers group before
    # dispatching the view to the client
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        # The below line overrides the queryset and filetrs it with the specific
        # maintenance record which is retreived from the url
        self.queryset = maintenancerecord.objects.filter(pk=self.kwargs['pk'])
        return super(HistoryDetails, self).dispatch(*args, **kwargs)
