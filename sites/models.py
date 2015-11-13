from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class site(AuthStampedModel,TimeStampedModel):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User)
    reportGroup = models.ForeignKey(Group)

    def __str__(self):
        return self.name
