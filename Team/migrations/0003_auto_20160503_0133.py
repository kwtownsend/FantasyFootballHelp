# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0002_auto_20160422_1954'),
        ('Team', '0002_auto_20160502_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerrequest',
            name='player',
        ),
        migrations.AddField(
            model_name='playerrequest',
            name='player',
            field=models.ManyToManyField(default=1, to='Players.Player'),
        ),
    ]
