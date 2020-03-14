# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 21:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='starRating',
            field=models.IntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1)]),
        ),
    ]
