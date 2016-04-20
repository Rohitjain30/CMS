# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0001_initial'),
        ('NewsFeed', '0004_auto_20160410_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=250)),
                ('startDateTime', models.DateTimeField(default=False)),
                ('endDateTime', models.DateTimeField(blank=True, default=False, null=True)),
                ('description', models.CharField(max_length=4000)),
                ('organisedBy', models.CharField(max_length=250)),
                ('email', models.EmailField(default=False, max_length=254)),
                ('fbEvent', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('mobile', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='event_mobile', to='Profiler.Mobile')),
            ],
        ),
    ]