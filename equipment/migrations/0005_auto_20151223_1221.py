# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_maintenanceschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenanceschedule',
            name='interval',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenanceschedule',
            name='nextdate',
            field=models.DateField(default=datetime.datetime(2015, 12, 23, 10, 21, 43, 412218, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
