# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audit_log.models.fields
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('departments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, null=True, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, null=True, max_length=40)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('nextmaintenancedate', models.DateField(verbose_name='Next Maintenance')),
                ('intervalType', models.CharField(max_length=50)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, verbose_name='created by', related_name='created_equipment_equipment_set')),
                ('department', models.ForeignKey(to='departments.department')),
                ('modified_by', audit_log.models.fields.LastUserField(editable=False, null=True, to=settings.AUTH_USER_MODEL, verbose_name='modified by', related_name='modified_equipment_equipment_set')),
                ('site', models.ForeignKey(to='sites.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
