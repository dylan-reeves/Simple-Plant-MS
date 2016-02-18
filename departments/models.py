from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from sites.models import site


# department model


class department(AuthStampedModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User)
    sites = models.ManyToManyField(site)

    def __str__(self):
        return self.name

class artisan(AuthStampedModel, TimeStampedModel):
    department = models.ForeignKey(department)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
