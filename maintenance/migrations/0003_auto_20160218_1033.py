# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_maintenancerecord_running'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerecord',
            name='notapplicable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenancerecord',
            name='stopped',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintenancerecord',
            name='running',
            field=models.BooleanField(),
        ),
    ]
