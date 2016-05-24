import datetime as dt

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q


from equipment.models import equipment, maintenanceschedule
from .forms import RecordForm
from .models import maintenancerecord, maintenancerecorddetails
from departments.models import artisan
# Create your views here.

#==============================================================================
#===============SUMMARY OF UPCOMING MAINTENANCE================================
#==============================================================================
# This view shows the next five maintnenace task according to the next SCHEDULED
# date for maintenance filetered byt the department membership of the user


class IndexView(generic.ListView):
    queryset = maintenanceschedule.objects.order_by('nextdate')[:5]
    template_name = 'maintenance/index.html'
    context_object_name = 'upcoming_maintenance'

    # Override the dispatch method to filter the objects according to the
    # department of the logged on user.
    def dispatch(self, request, *args, **kwargs):
        # Get the departments the user is a member of
        UserDepartments = request.user.usermain.departments.all()
        # Assign a vaible to hold the query builder
        byDepartmentQuery = Q()
        # Loop through users departments to get the equipment
        # that belongs to the users departments
        for Department in UserDepartments:
            byDepartmentQuery = byDepartmentQuery | Q(department=Department)
        # Populate the queryset using the output of the query builder.
        # retreive all the equipment and store in the below variable
        userEquipment = equipment.objects.filter(byDepartmentQuery)
        # Now we create a byEquipment variable to hold the query builder
        byEquipmentQuery = Q()
        # Loop through the equipment to build a query
        for userDeptEquipment in userEquipment:
            byEquipmentQuery = byEquipmentQuery | Q(
                equipment=userDeptEquipment)
        self.queryset = maintenanceschedule.objects.filter(
            byEquipmentQuery).order_by('nextdate')[:5]
        return super(IndexView, self).dispatch(request, *args, **kwargs)

#==============================================================================
#===============EXECUTE MAINTENANCE VIEW=======================================
#==============================================================================
# This view handles the creation of the form to record the actual execution of a
# maintenance job


def ExecuteView(request, pk):
    # stores the maintenance shcedule record in a variable
    maintjobrec = maintenanceschedule.objects.get(pk=pk)
    # The else argument will service the POST request, here it creates an
    # instance of the form and passes the maintenancejob primarykey and the
    # equipment primary key to the form as the form will be generated according
    # to the items in the database
    if request.method == 'POST':
        form = RecordForm(
            request.POST, prikey=maintjobrec.maintenancejob, equipid=maintjobrec.equipment.id)
        if form.is_valid():
            # If the form is vaild start saving the information to the database
            # First create a record item for the main maintenance record
            record = maintenancerecord(equipment=maintjobrec.equipment,
                                       maintjob=maintjobrec.maintenancejob,
                                       maintenancedate=dt.date.today(),
                                       artisan=artisan.objects.get(
                                           pk=form['artisan'].value),
                                       running=request.POST.get('running'),
                                       stopped=request.POST.get('stopped'),
                                       notapplicable=request.POST.get('na'),
                                       comments=request.POST.get('generalcomments'))
            # save the main maintenance record
            record.save()
            # Now the form will loop through the posted items to capture the task
            # details for the maintenance job
            for key, value in request.POST.items():
                ifcomment = key
                # checks to see if the specific item name starts with comment_
                # if this is true the details are saved to the database
                if ifcomment.startswith("completed"):
                    # the maintenance record for the foreign key
                    maintenancerecordid = record
                    # loops through the feilds of the form to find the feild name
                    # that matches the key value
                    for field in form:
                        if field.name == key:
                            # Grab the label from the matching form to put in
                            # detail
                            detailtaskdescription = field.label
                    # The detail of the comment feild to store in the database
                    detailcompleted = value
                    # get the number of the the item to get the corresponding comment
                    # this is stripped off the end of the comment string as the string
                    # names will go completed_1 completed_2 completed_3 etc
                    itemnumber = key.split("_", 1)[1]
                    # set the details of the comment equal to the ...
                    detailcomment = request.POST['comment_' + itemnumber]
                    # create the record for the detail
                    detailrecord = maintenancerecorddetails(maintenancerecord=maintenancerecordid,
                                                            taskdetail=detailtaskdescription,
                                                            completed=detailcompleted,
                                                            comment=detailcomment)
                    detailrecord.save()
            # Set the maintenance previous date of maintenance to the current
            # date
            maintjobrec.previousdate = dt.date.today()
            # Add the service interval tot he current date and set the nextdate
            # maintenance date
            maintjobrec.nextdate = dt.date.today() + dt.timedelta(days=maintjobrec.interval)
            maintjobrec.save()
            return HttpResponseRedirect('/maintenance/')
    else:
        # The else argument will service the GET request, here it creates an
        # instance of the form and passes the maintenancejob primarykey and the
        # equipment primary key to the form as the form will be generated according
        # to the items in the database
        form = RecordForm(prikey=maintjobrec.maintenancejob,
                          equipid=maintjobrec.equipment.id)

    return render(request, 'maintenance/execute.html', {'form': form})
