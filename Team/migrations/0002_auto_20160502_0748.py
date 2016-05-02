# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0002_auto_20160422_1954'),
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='policies',
        ),
        migrations.AddField(
            model_name='playerrequest',
            name='player',
            field=models.ForeignKey(default=1, to='Players.Player'),
        ),
    ]
