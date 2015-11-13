# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import audit_log.models.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(editable=False, null=True, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(editable=False, null=True, max_length=40)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_departments_department_set', null=True, editable=False, to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_departments_department_set', null=True, editable=False, to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
                ('sites', models.ManyToManyField(to='sites.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
