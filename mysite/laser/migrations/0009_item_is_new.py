# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laser', '0008_newsarticle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
