# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_horsetestdata_fixture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixturetestdata',
            name='html_row',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='horsetestdata',
            name='html_row',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resulttestdata',
            name='html_row',
            field=models.TextField(null=True),
        ),
    ]