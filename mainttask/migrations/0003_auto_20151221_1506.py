# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainttask', '0002_auto_20151221_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceTaskDetailItems',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, max_length=40, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, max_length=40, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('task', models.CharField(max_length=250)),
                ('created_by', audit_log.models.fields.CreatingUserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, related_name='created_mainttask_maintenancetaskdetailitems_set', verbose_name='created by')),
                ('maintjob', models.ForeignKey(null=True, to='mainttask.MaintenanceJob', blank=True)),
                ('modified_by', audit_log.models.fields.LastUserField(null=True, to=settings.AUTH_USER_MODEL, editable=False, related_name='modified_mainttask_maintenancetaskdetailitems_set', verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='maintenancetaskdetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='maintenancetaskdetail',
            name='maintjob',
        ),
        migrations.RemoveField(
            model_name='maintenancetaskdetail',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='MaintenanceTaskDetail',
        ),
    ]
