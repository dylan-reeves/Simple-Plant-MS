from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class MaintenanceTaskDetail(AuthStampedModel,TimeStampedModel):
    task = models.CharField(max_length=250)
    def __str__(self):
        return self.task

class MaintenanceJob(AuthStampedModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    tasks = models.ForeignKey(MaintenanceTaskDetail, null=True, blank=True)
    def __str__(self):
        return self.name
