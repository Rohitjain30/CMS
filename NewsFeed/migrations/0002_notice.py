# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_auto_20160410_1530'),
        ('NewsFeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('issuingAuthority', models.CharField(max_length=250)),
                ('issueDate', models.DateTimeField(auto_now_add=True)),
                ('fileLink', models.URLField(blank=True, null=True)),
                ('branch', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.Branch')),
                ('degree', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.Degree')),
                ('department', models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='Course.Department')),
            ],
        ),
    ]