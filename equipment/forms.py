from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import equipment

class CreateEquipmentForm(ModelForm):
    class Meta:
        model = equipment
        fields = ['name', 'code', 'site', 'department', 'nextmaintenancedate', 'intervalType', 'active']

    def __init__(self, *args, **kwargs):
        super(CreateEquipmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('nextmaintenancedate', id='checkthisworks', type='date',)
        )
