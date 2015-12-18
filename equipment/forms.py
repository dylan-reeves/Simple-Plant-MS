from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import equipment

class CreateEquipmentForm(ModelForm):
    class Meta:
        model = equipment
        fields = ['name', 'code', 'site', 'department', 'nextmaintenancedate', 'intervalType', 'active']
