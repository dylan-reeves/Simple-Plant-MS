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
#Views that handle all the actions to do with the equipment in the system

#The below method is to check that the user is a member of the superadmin or the
#manager group in order to be able to add/update/remove equipment, does not
#require a separate method for CRUD and both groups can perform all actions

def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'manager']).exists()

#=============================================================================
#=========================GENERIC EQUIPMENT LIST VIEW=========================
#=============================================================================
#This view is the default landing page for the equipment view and will display
#all equipment for the users department

class IndexView(generic.ListView):
    model = equipment
    template_name = 'equipment/index.html'
    context_object_name = 'equipment_details'

    #Check to see if the user is logged in as superadmin or manager
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied'))
    def dispatch(self, request, *args, **kwargs):
        #populate the queryset from the equipment model and filter the response
        #according to the department membership of the user

        #get the departments the user is a member of
        UserDepartments = request.user.usermain.departments.all()
        #Assign the variable to hold the context object which will be created by
        #the Q function
        byDepartmentQuery = Q()
        #Now loop through all the users departments and get the equipment
        #assigned to that department and add it to the query object
        for Department in UserDepartments:
            byDepartmentQuery = byDepartmentQuery | Q(department=Department)
        #populate the queryset according to the Department Query
        self.queryset = equipment.objects.filter(byDepartmentQuery)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

#==============================================================================
#====================EQUIPMENT DETAILS VIEW====================================
#==============================================================================

#Displays all the fields of a single department entry
class DetailView(generic.DetailView):
    model = equipment
    template_name = 'equipment/details.html'
    context_object_name = 'equipment_details'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        prikey = self.kwargs['pk']
        context['schedule_list'] = maintenanceschedule.objects.filter(equipment = prikey)
        return context

#Loads and handles the form to create a new department
class CreateView(generic.CreateView):
    model = equipment
    template_name = 'equipment/create.html'
    fields = ['name', 'code', 'site', 'department',  'active']
    success_url = '/equipment/'

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)
#Loads and handles the departments update
class UpdateView(generic.UpdateView):
    model = equipment
    fields = ['name', 'code', 'site', 'department',  'active']
    template_name = 'equipment/update.html'
    success_url = '/equipment/'

#Displays the department delete confirmation page
class DeleteView(generic.DeleteView):
    model = equipment
    success_url = '/equipment/'
    template_name = 'equipment/delete.html'
    context_object_name = 'equipment_details'

class AddScheduleView(generic.CreateView):
    model = maintenanceschedule
    template_name = 'equipment/addschedule.html'
    fields = ['maintenancejob', 'interval', 'nextdate']
    success_url = '/equipment/'

    def form_valid(self, form):
        schedule = form.save(commit=False)
        equip = equipment.objects.get(pk=self.kwargs['pk'])
        schedule.equipment = equip
        return super(AddScheduleView, self).form_valid(form)

class UpdateScheduleView(generic.UpdateView):
    model = maintenanceschedule
    template_name = 'equipment/update.html'
    fields = ['maintenancejob', 'interval']
    success_url = '/equipment/'

class DeleteScheduleView(generic.DeleteView):
    model = maintenanceschedule
    template_name = 'equipment/deleteschedule.html'
    context_object_name = 'schedule_details'
    success_url = '/equipment/'

class MaintHistory(generic.ListView):
    template_name ='equipment/mainthistory.html'
    context_object_name = 'mainthistory'
    def dispatch(self, *args, **kwargs):
        self.queryset = maintenancerecord.objects.filter(equipment=self.kwargs['pk'])
        return super(MaintHistory, self).dispatch(*args, **kwargs)

class HistoryDetails(generic.DetailView):
    template_name='equipment/mainthistorydetails.html'
    context_object_name = 'mainthistory'

    def get_context_data(self,**kwargs):
        context = super(HistoryDetails, self).get_context_data(**kwargs)
        context['mainthistorydetails'] = maintenancerecorddetails.objects.filter(maintenancerecord=self.kwargs['pk'])
        return context

    def dispatch(self, *args, **kwargs):
        self.queryset = maintenancerecord.objects.filter(pk=self.kwargs['pk'])
        return super(HistoryDetails, self).dispatch(*args, **kwargs)
