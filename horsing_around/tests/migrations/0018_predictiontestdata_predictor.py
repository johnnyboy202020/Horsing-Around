# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0017_auto_20171030_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictiontestdata',
            name='predictor',
            field=models.CharField(default='LinearRegression', max_length=50),
            preserve_default=False,
        ),
    ]