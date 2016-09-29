# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20160922_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_photo',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=registration.models.upload_location, width_field='width_field'),
        ),
    ]