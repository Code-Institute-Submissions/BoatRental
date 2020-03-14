# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedBoat',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='boats',
            options={
                'verbose_name_plural': 'Boats'},
        ),
        migrations.AddField(
            model_name='featuredboat',
            name='boat',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='boats.Boats'),
        ),
    ]
