# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20160218_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerecord',
            name='artisan',
            field=models.ForeignKey(to='departments.artisan'),
        ),
    ]
