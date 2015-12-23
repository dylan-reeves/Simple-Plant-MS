from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel

from equipment.models import equipment
from mainttask.models import MaintenanceJob

# Create your models here.
class maintenanceschedule(AuthStampedModel, TimeStampedModel):
    equipment = models.ForeignKey(equipment)
    maintenancejob = models.ForeignKey(MaintenanceJob)
    interval = models.IntegerField
    previousdate = models.DateField(null=True)
    nextdate = models.DateField
