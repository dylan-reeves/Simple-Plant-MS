from django import forms

from equipment.models import equipment, maintenanceschedule
from .models import maintenancerecord, maintenancerecorddetails
from

class RecordForm(forms.ModelForm):
    class Meta:
        model = maintenancerecord
