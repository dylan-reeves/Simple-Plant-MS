from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from equipment.models import equipment, maintenanceschedule
from .forms import RecordForm
# Create your views here.
class IndexView(generic.ListView):
    queryset = maintenanceschedule.objects.order_by('nextdate')[:5]
    template_name = 'maintenance/index.html'
    context_object_name = 'upcoming_maintenance'

class ExecuteView(generic.edit.FormView):
    template_name = 'maintenance/execute.html'
    success_url = '/maintenance/'
    form_class = RecordForm
    def dispatch(self, *args, **kwargs):
        form_class = RecordForm(my_arg=self.kwargs['pk'])
        return super(ExecuteView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.printsuccess()
        return super(ExecuteView, self).form_valid(form)
