# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0001_initial'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='maintenancejobs',
            field=models.ManyToManyField(blank=True, null=True, to='mainttask.MaintenanceJob'),
        ),
    ]
