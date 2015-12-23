# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import audit_log.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainttask', '0005_auto_20151222_1004'),
        ('equipment', '0003_auto_20151223_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenanceschedule',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('previousdate', models.DateField(null=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_maintsched_maintenanceschedule_set', verbose_name='created by', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('equipment', models.ForeignKey(to='equipment.equipment')),
                ('maintenancejob', models.ForeignKey(to='mainttask.MaintenanceJob')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_maintsched_maintenanceschedule_set', verbose_name='modified by', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
