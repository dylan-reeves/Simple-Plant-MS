from django import forms

from equipment.models import equipment, maintenanceschedule
from .models import maintenancerecord, maintenancerecorddetails
from mainttask.models import MaintenanceJob, MaintenanceTaskDetailItems
from departments.models import artisan

class RecordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        pknumber = kwargs.pop('prikey')
        pkequip = kwargs.pop('equipid')
        super(RecordForm, self).__init__(*args, **kwargs)
        tasks = MaintenanceTaskDetailItems.objects.filter(maintjob=pknumber).order_by('orderfield')
        Completed = 'OK'
        NotCompleted = 'NO'
        NotApplicable = 'NA'
        completed_choices = (
            (Completed, 'OK'),
            (NotCompleted, 'NO'),
            (NotApplicable, 'NA'),
            )

        itemnumber=1
        for task in tasks:
            self.fields["completed_%d" % itemnumber] = forms.ChoiceField(choices=completed_choices, label=task.task)
            self.fields["comment_%d" % itemnumber] = forms.CharField()
            itemnumber = itemnumber + 1


        dept = equipment.objects.get(pk=pkequip).department


        self.fields["artisan"] = forms.ModelChoiceField(queryset=artisan.objects.filter(department=dept))
        self.fields["running"] = forms.BooleanField(required=False,initial=False)
        self.fields["stopped"] = forms.BooleanField(required=False,initial=False)
        self.fields["na"] = forms.BooleanField(required=False,initial=False)
        self.fields["generalcomments"] = forms.CharField()

    def printsuccess(self):
        pass
