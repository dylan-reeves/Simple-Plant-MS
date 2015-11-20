from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from sites.models import site

#Department Model Manger to filter department results
#class DepartmentUserFilter(models.Manager):
    #def get_queryset(self, user):
        #userSite = user.profile.site
        #return Super(DepartmentUserFilter,self).get_queryset().filter(sites = userSite)

#department model
class department(AuthStampedModel,TimeStampedModel):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User)
    sites = models.ManyToManyField(site)

    #for_user = DepartmentUserFilter()
    def __str__(self):
        return self.name
