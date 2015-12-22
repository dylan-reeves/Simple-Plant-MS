# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0004_maintenancetaskdetailitems_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maintenancetaskdetailitems',
            old_name='order',
            new_name='orderfield',
        ),
    ]
