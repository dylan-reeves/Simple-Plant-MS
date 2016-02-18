import datetime as dt

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


from equipment.models import equipment, maintenanceschedule
from .forms import RecordForm
from .models import maintenancerecord, maintenancerecorddetails
from departments.models import artisan
# Create your views here.
class IndexView(generic.ListView):
    queryset = maintenanceschedule.objects.order_by('nextdate')[:5]
    template_name = 'maintenance/index.html'
    context_object_name = 'upcoming_maintenance'

def ExecuteView(request, pk):
    maintjobrec = maintenanceschedule.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST,prikey=maintjobrec.maintenancejob, equipid=maintjobrec.equipment.id )
        if form.is_valid():
            print(form)
            record = maintenancerecord(equipment=maintjobrec.equipment,
                                        maintjob=maintjobrec.maintenancejob,
                                        maintenancedate=dt.date.today(),
                                        artisan=artisan.objects.get(pk=form['artisan'].value),
                                        running=request.POST.get('running'),
                                        stopped=request.POST.get('stopped'),
                                        notapplicable=request.POST.get('na'),
                                        comments=request.POST.get('generalcomments'))
            record.save()
            for key, value in request.POST.items():
                ifcomment = key
                if ifcomment.startswith("completed"):
                    #the maintenance record for the foreign key
                    detailrecord = record
                    for field in form:
                        if field.name == key:
                            #Grab the label from the matching form to put in detail
                            detailtaskdescription = field.label
                    detailcompleted = value
                    #get the number of the the item to get the corresponding comment
                    itemnumber = key.split("_",1)[1]
                    detailcomment = request.POST['comment_' + itemnumber]
                    detailrecord = maintenancerecorddetails(maintenancerecord=detailrecord,
                                                            taskdetail=detailtaskdescription,
                                                            completed=detailcompleted,
                                                            comment=detailcomment)
                    detailrecord.save()
            nextmaintenancedate = dt.date.today()
            maintenanceinterval = maintjobrec.interval
            maintjobrec.previousdate = nextmaintenancedate
            maintjobrec.nextdate = nextmaintenancedate + dt.timedelta(days=maintenanceinterval)
            maintjobrec.save()


            return HttpResponseRedirect('/maintenance/')
    else:
        form = RecordForm(prikey=maintjobrec.maintenancejob,equipid=maintjobrec.equipment.id)

    return render(request, 'maintenance/execute.html', {'form': form})
