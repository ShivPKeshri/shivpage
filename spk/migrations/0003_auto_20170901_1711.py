# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spk', '0002_auto_20170901_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgblog',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]