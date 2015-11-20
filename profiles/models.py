from django.db import models
from django.contrib.auth.models import User

from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel

from sites.models import site
from departments.models import department

# Create your models here.
class userProfile(AuthStampedModel,TimeStampedModel):
    user = models.OneToOneField(User, primary_key=True)
    departments = models.ManyToManyField(department)
    sites = models.ManyToManyField(site)
    def __str__(self):
        return self.user.username
