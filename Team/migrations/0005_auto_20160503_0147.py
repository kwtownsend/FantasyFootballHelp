# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0002_auto_20160422_1954'),
        ('Team', '0004_auto_20160503_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerrequest',
            name='player',
        ),
        migrations.AddField(
            model_name='playerrequest',
            name='player',
            field=models.ManyToManyField(to='Players.Player'),
        ),
    ]
