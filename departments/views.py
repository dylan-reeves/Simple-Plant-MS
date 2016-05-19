from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from .models import department, artisan
from equipment.models import equipment
from sites.models import site

#=======================DEPARTMENTS VIEWS======================================
# Default landing page for departments app simply displays a clickable
# list of departments

# This method just check to see if the user is a member of the superadmin or
# manager group as these are the only gourps that are allowed to view
# departments


def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['superadmin', 'manager']).exists()

# This mothod checks to see if the user is a memeber of the superadmin groups
# as only the superadmin can create edit and delete departments


def is_in_multiple_groups_CRUD(user):
    return user.groups.filter(name__in=['superadmin']).exists()

#==============================================================================
#==================GENERIC DEPARTMENT LIST VIEW================================
#=============================================================================


class IndexView(generic.ListView):
    #model = department
    template_name = 'departments/index_admin.html'
    context_object_name = 'department_list'
    # check to see if logged on user is superadmin or manager otherwise send
    # to access denied

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, request, *args, **kwargs):
        # populate the queryset and filter the departments viewable according
        # to the departments the user is a member of
        self.queryset = department.objects.filter(
            usr_dept=request.user.usermain)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

#==============================================================================
#=====================SPECIFIC DEPARTMENT DETAILS VIEW=========================
#==============================================================================
# Displays all the fields of a single department entry called by clicking on
# the hyperlink in the generic view created above


class DetailView(generic.DetailView):
    model = department
    template_name = 'departments/details.html'
    context_object_name = 'department_details'
    # This detail view also displays all the equipment assigned to a department
    # and the various artisans assigned to the department, the get_context_data
    # below creates two addtional context items to display this data

    def get_context_data(self, **kwargs):
        # this creates the default context from the department model
        context = super(DetailView, self).get_context_data(**kwargs)
        # This variable is used to store the pk argument from the url which
        # relates to the primary key for the department to allow filtering of
        #artisans and equipment
        prikey = self.kwargs['pk']
        # this will get the list of equipment assigned to the department defined
        # by the prikey variable
        context['equipment_list'] = equipment.objects.filter(department=prikey)
        # this will get the list of artisans assigned to the department defined
        # by the prikey variable
        context['artisans'] = artisan.objects.filter(department=prikey)
        return context

    # The method decorator will check to see if the user is a member of the
    # manager or the superadmin group before serving the view
    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

#==============================================================================
#======================CREATE DEPARTMENT VIEW==================================
#==============================================================================

# Loads and handles the form to create a new department


class CreateView(generic.CreateView):
    model = department
    template_name = 'departments/create.html'
    fields = ['name', 'manager', 'sites']
    success_url = '/departments/'

    # this methods checks that the user is a member of the superadmin group before
    # enabling access to create additional departments
    @method_decorator(user_passes_test(is_in_multiple_groups_CRUD, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

#==============================================================================
#====================UPDATE DEPARTMENT VIEW====================================
#==============================================================================
# Loads and handles the departments update


class UpdateView(generic.UpdateView):
    model = department
    fields = ['name', 'manager', 'sites']
    template_name = 'departments/update.html'
    success_url = '/departments/'
    # the method decorator ensure the user is a member of the superadmin group in
    # order to make updates to the department

    @method_decorator(user_passes_test(is_in_multiple_groups_CRUD, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

#==============================================================================
#======================DELETE DEPARTMENT VIEW==================================
#==============================================================================
# Displays the department delete confirmation page


class DeleteView(generic.DeleteView):
    model = department
    success_url = '/departments/'
    template_name = 'departments/delete.html'
    context_object_name = 'department_details'
    # Check that the logged on user is a member of the superadmin group as only
    # members of this group can delete departments

    @method_decorator(user_passes_test(is_in_multiple_groups_CRUD, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

#==============================================================================
#==================VIEW TO CREATE ARTISANS=====================================
#==============================================================================
# This view is used to create departments for the the selected department
# Artisans are used when recording a specific maintenance job as the actual
# people who conduct the work


class CreateArtisanView(generic.CreateView):
    model = artisan
    template_name = 'departments/createartisan.html'
    fields = ['name']
    # this checks to make sure the user is in the superadmin or the manager
    # group

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        return super(CreateArtisanView, self).dispatch(*args, **kwargs)

    # the form_valid method gets the department primary key from the url argument
    # and stores it in the variable depart. Which is then used as the foreign key
    # when creating the artisan, on success the user is then redirected to the
    # details for the department
    def form_valid(self, form):
        artisan = form.save(commit=False)
        depart = department.objects.get(pk=self.kwargs['pk'])
        artisan.department = depart
        self.success_url = '/departments/' + self.kwargs['pk']
        return super(CreateArtisanView, self).form_valid(form)

#==============================================================================
#=====================UPDATE ARTISANS VIEW=====================================
#==============================================================================
# This view is used to edit existing artisans for the selected department


class UpdateArtisanView(generic.UpdateView):
    model = artisan
    fields = ['name']
    template_name = 'departments/updateartisan.html'
    # this checks to see that the user is a member of the superadmin or the manager
    # group in order to update

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        # the prikey variable is used to redirect the user to the calling
        # department on success
        prikey = artisan.objects.get(pk=self.kwargs['pk'])
        self.success_url = '/departments/' + str(prikey.department.id)
        return super(UpdateArtisanView, self).dispatch(*args, **kwargs)

#==============================================================================
#=========================DELETE AN ARTISAN====================================
#==============================================================================
# This view is used to delete artisans


class DeleteArtisanView(generic.DeleteView):
    model = artisan
    template_name = 'departments/deleteartisan.html'
    context_object_name = 'artisan'
    # Check to see if the user is a member of superadmin or manager

    @method_decorator(user_passes_test(is_in_multiple_groups, login_url='/accounts/denied/'))
    def dispatch(self, *args, **kwargs):
        # the prikey is used to get the department of the artisan and is used in
        # success url to redirect the user to the details page for the
        # department
        prikey = artisan.objects.get(pk=self.kwargs['pk'])
        self.success_url = '/departments/' + str(prikey.department.id)
        return super(DeleteArtisanView, self).dispatch(*args, **kwargs)
