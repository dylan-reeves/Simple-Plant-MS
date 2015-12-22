# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0003_auto_20151221_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancetaskdetailitems',
            name='order',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
