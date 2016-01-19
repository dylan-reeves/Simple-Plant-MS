from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from equipment.models import equipment, maintenanceschedule
from .forms import RecordForm
from .models import maintenancerecord, maintenancerecorddetails
# Create your views here.
class IndexView(generic.ListView):
    queryset = maintenanceschedule.objects.order_by('nextdate')[:5]
    template_name = 'maintenance/index.html'
    context_object_name = 'upcoming_maintenance'

def ExecuteView(request, pk):
    if request.method == 'POST':
        form = RecordForm(prikey=pk)
        if form.is_valid():
            record = maintenancerecord()
            return HttpResponseRedirect('/maintenance/')
    else:
        form = RecordForm(prikey=pk)
    equipment_id = 
    record_info = (

    )
    return render(request, 'maintenance/execute.html', {'form': form,
                                                        'record_info': record_info } )
