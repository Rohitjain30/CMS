# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-09 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.CharField(max_length=20)),
                ('semester', models.IntegerField()),
                ('startRollNo', models.CharField(max_length=20)),
                ('endRollNo', models.CharField(max_length=20)),
                ('strength', models.PositiveIntegerField()),
                ('branch', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Branch')),
            ],
        ),
    ]
