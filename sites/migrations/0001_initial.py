# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='created_sites_site_set', verbose_name='created by')),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('modified_by', audit_log.models.fields.LastUserField(null=True, editable=False, to=settings.AUTH_USER_MODEL, related_name='modified_sites_site_set', verbose_name='modified by')),
                ('reportGroup', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
