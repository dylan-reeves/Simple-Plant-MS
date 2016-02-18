# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerecord',
            name='running',
            field=models.CharField(default='NA', max_length=20),
            preserve_default=False,
        ),
    ]
