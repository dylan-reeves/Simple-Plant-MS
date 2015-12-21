# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenancetaskdetail',
            name='maintjobname',
        ),
        migrations.AddField(
            model_name='maintenancetaskdetail',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenancetaskdetail',
            name='maintjob',
            field=models.ForeignKey(blank=True, null=True, to='mainttask.MaintenanceJob'),
        ),
    ]
