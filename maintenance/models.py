from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel

from equipment.models import equipment
from mainttask.models import MaintenanceJob
from departments.models import artisan

# Create your models here.
class maintenancerecord(AuthStampedModel,TimeStampedModel):
    equipment = models.ForeignKey(equipment)
    maintjob = models.ForeignKey(MaintenanceJob)
    maintenancedate = models.DateField()
    artisan = models.ForeignKey(artisan)
    running = models.NullBooleanField(default=False)
    stopped = models.NullBooleanField(default=False)
    notapplicable = models.NullBooleanField(default=False)
    comments = models.TextField()

class maintenancerecorddetails(AuthStampedModel, TimeStampedModel):
    maintenancerecord = models.ForeignKey(maintenancerecord)
    taskdetail = models.CharField(max_length=150)
    completed = models.CharField(max_length=150)
    comment = models.TextField(null=True)
