# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nflstats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
                ('fpts', models.FloatField()),
                ('fptsg', models.FloatField()),
                ('gp', models.FloatField()),
                ('pyds', models.FloatField()),
                ('ptd', models.FloatField()),
                ('ryd', models.FloatField()),
                ('rtd', models.FloatField()),
                ('recyds', models.FloatField()),
                ('rectd', models.FloatField()),
                ('fum', models.FloatField()),
                ('sack', models.FloatField()),
                ('fr', models.FloatField()),
                ('intercept', models.FloatField()),
                ('td', models.FloatField()),
                ('sfty', models.FloatField()),
                ('fg', models.FloatField()),
                ('fgmiss', models.FloatField()),
                ('xpt', models.FloatField()),
            ],
        ),
    ]
