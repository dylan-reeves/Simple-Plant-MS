# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audit_log.models.fields
import django_extensions.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, max_length=40, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, max_length=40, editable=False)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_profiles_userprofile_set', verbose_name='created by', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('departments', models.ManyToManyField(to='departments.department')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_profiles_userprofile_set', verbose_name='modified by', null=True, to=settings.AUTH_USER_MODEL, editable=False)),
                ('sites', models.ManyToManyField(to='sites.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
