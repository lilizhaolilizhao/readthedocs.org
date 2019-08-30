# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-29 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0044_auto_20190703_1300'),
        ('builds', '0010_add-description-field-to-automation-rule'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('path', models.CharField(max_length=4096)),
                ('view_count', models.PositiveIntegerField(default=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_views', to='projects.Project')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_views', to='builds.Version', verbose_name='Version')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]