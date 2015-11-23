from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import site

# Register your models here.
admin.site.register(site)
admin.site.register(Permission)
