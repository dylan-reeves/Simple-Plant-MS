# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='artisan',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, editable=False, max_length=40)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, editable=False, max_length=40)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, related_name='created_departments_artisan_set', editable=False, verbose_name='created by', null=True)),
                ('department', models.ForeignKey(to='departments.department')),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, related_name='modified_departments_artisan_set', editable=False, verbose_name='modified by', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
