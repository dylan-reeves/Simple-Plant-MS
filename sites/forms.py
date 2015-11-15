from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import site

class siteForm(ModelForm):
    class Meta:
        model = site
        fields = ['name', 'manager', 'reportGroup']

    def __init__(self,*args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Submit'))
        super(siteForm, self).__init__(*args, **kwargs)
