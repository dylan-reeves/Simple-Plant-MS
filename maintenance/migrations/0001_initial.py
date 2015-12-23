# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import audit_log.models.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainttask', '0005_auto_20151222_1004'),
        ('equipment', '0005_auto_20151223_1221'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenancerecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('maintenancedate', models.DateField()),
                ('artisan', models.CharField(max_length=150)),
                ('comments', models.TextField()),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_maintenance_maintenancerecord_set', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('equipment', models.ForeignKey(to='equipment.equipment')),
                ('maintjob', models.ForeignKey(to='mainttask.MaintenanceJob')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_maintenance_maintenancerecord_set', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='maintenancerecorddetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('taskdetail', models.CharField(max_length=150)),
                ('completed', models.CharField(max_length=150)),
                ('comment', models.TextField(null=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_maintenance_maintenancerecorddetails_set', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='created by')),
                ('maintenancerecord', models.ForeignKey(to='maintenance.maintenancerecord')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_maintenance_maintenancerecorddetails_set', to=settings.AUTH_USER_MODEL, editable=False, null=True, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
