# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import audit_log.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceJob',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaintenanceTaskDetail',
            fields=[
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, max_length=40, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, max_length=40, null=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('maintjobname', models.OneToOneField(primary_key=True, to='mainttask.MaintenanceJob', serialize=False)),
                ('task', models.CharField(max_length=250)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='created by', related_name='created_mainttask_maintenancetaskdetail_set', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='modified by', related_name='modified_mainttask_maintenancetaskdetail_set', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='maintenancejob',
            name='created_by',
            field=audit_log.models.fields.CreatingUserField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='created by', related_name='created_mainttask_maintenancejob_set', null=True),
        ),
        migrations.AddField(
            model_name='maintenancejob',
            name='modified_by',
            field=audit_log.models.fields.LastUserField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='modified by', related_name='modified_mainttask_maintenancejob_set', null=True),
        ),
    ]
