from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from sites.models import site

#class deptsManager(models.Manager):
    #def by_group(self):

# department model


class department(AuthStampedModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User)
    sites = models.ManyToManyField(site)

    #for_user = DepartmentUserFilter()
    def __str__(self):
        return self.name
