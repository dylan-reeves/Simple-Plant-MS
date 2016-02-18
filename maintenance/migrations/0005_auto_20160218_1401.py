# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20160218_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerecord',
            name='notapplicable',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='maintenancerecord',
            name='running',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='maintenancerecord',
            name='stopped',
            field=models.NullBooleanField(default=False),
        ),
    ]
