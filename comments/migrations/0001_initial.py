# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boats', '0002_auto_20200307_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentText', models.CharField(default='', max_length=254)),
                ('date', models.DateField(auto_now=True)),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.Boats')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]