# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
        ('Profiler', '__first__'),
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('documentId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.PositiveIntegerField(choices=[(0, 'Word Document'), (1, 'Text File'), (2, 'Presentation'), (3, 'PDF')])),
                ('source', models.FileField(upload_to='Document')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publicationId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('authors', models.CharField(max_length=50)),
                ('publicationDate', models.DateField()),
                ('organization', models.CharField(max_length=50)),
                ('webLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resourceId', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.PositiveIntegerField(choices=[(0, 'Book'), (1, 'Publication'), (2, 'Document'), (3, 'Web Links')])),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
                ('updatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profiler.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('webLinkId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('link', models.URLField()),
            ],
        ),
    ]
