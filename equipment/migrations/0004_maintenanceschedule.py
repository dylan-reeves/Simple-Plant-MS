# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0005_auto_20151222_1004'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0003_auto_20151223_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenanceschedule',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('previousdate', models.DateField(null=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_equipment_maintenanceschedule_set', null=True, verbose_name='created by', to=settings.AUTH_USER_MODEL, editable=False)),
                ('equipment', models.ForeignKey(to='equipment.equipment')),
                ('maintenancejob', models.ForeignKey(to='mainttask.MaintenanceJob')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_equipment_maintenanceschedule_set', null=True, verbose_name='modified by', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
