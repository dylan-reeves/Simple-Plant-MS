from django import forms



class CopyForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    
