from django.template import Library
from datetime import date, timedelta

register = Library()

@register.filter(name='get_range_colour_code')
def get_range_colour_code( value ):
    maintenanceDate = value
    if maintenanceDate < date.today():
        return "danger"
    elif maintenanceDate >= date.today() and maintenanceDate <= date.today() + timedelta(days=7):
        return "warning"
    elif maintenanceDate > date.today() + timedelta(days=7):
        return "success"
