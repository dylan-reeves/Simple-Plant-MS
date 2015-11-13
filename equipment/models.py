from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from sites.models import site
from departments.models import department

# Create your models here.
class equipment(AuthStampedModel,TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    site = models.ForeignKey(site)
    department = models.ForeignKey(department)
    #TODO add jobs foreign key
    #next maintenance date will be calculated when the maintenance jobs recorded
    nextmaintenancedate = models.DateField('Next Maintenance')
    intervalType = models.CharField(max_length=50)
    active = models.BooleanField('Active', default=True)
    def __str__(self):
        return self.name
