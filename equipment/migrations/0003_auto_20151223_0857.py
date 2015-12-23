# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equipment_maintenancejobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='intervalType',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='maintenancejobs',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='nextmaintenancedate',
        ),
    ]
