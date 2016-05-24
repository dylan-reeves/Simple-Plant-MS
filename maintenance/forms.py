from django import forms

from equipment.models import equipment, maintenanceschedule
from .models import maintenancerecord, maintenancerecorddetails
from mainttask.models import MaintenanceJob, MaintenanceTaskDetailItems
from departments.models import artisan

# This class holds the form for the execution of a maintenance task, the form is
# generated at runtime


class RecordForm(forms.Form):
    # override the initialization method for the form

    def __init__(self, *args, **kwargs):
        # Get the primary key of the maintenance job from the calling view
        pknumber = kwargs.pop('prikey')
        # Get the equipment ID from the calling view
        pkequip = kwargs.pop('equipid')
        super(RecordForm, self).__init__(*args, **kwargs)
        # get the maintenance tasks for the maintenance job and store in the
        # tasks variable
        tasks = MaintenanceTaskDetailItems.objects.filter(
            maintjob=pknumber).order_by('orderfield')
        # create the options for the drop down box and store in a coices list
        Completed = 'OK'
        NotCompleted = 'NO'
        NotApplicable = 'NA'
        completed_choices = (
            (Completed, 'OK'),
            (NotCompleted, 'NO'),
            (NotApplicable, 'NA'),
        )
        # Create itemnumber placeholder to differentiate the fields to be
        # created
        itemnumber = 1
        # Loop through the maintenance tasks
        for task in tasks:
            # create a field that will be a drop down set to the choices
            self.fields["completed_%d" % itemnumber] = forms.ChoiceField(
                choices=completed_choices, label=task.task)
            # create the field that will be filled in by the artisan
            self.fields["comment_%d" % itemnumber] = forms.CharField()
            itemnumber = itemnumber + 1
        # get the department of the peice of equipment
        dept = equipment.objects.get(pk=pkequip).department
        # Use the department variable from above to populate choice field with
        # artisans for the department
        self.fields["artisan"] = forms.ModelChoiceField(
            queryset=artisan.objects.filter(department=dept))
        # The rest of the field s are static and the same for each
        self.fields["running"] = forms.BooleanField(
            required=False, initial=False)
        self.fields["stopped"] = forms.BooleanField(
            required=False, initial=False)
        self.fields["na"] = forms.BooleanField(required=False, initial=False)
        self.fields["generalcomments"] = forms.CharField()

    def printsuccess(self):
        pass
