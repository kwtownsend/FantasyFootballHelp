# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Queue', '0002_auto_20160502_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='owner',
            new_name='leader',
        ),
    ]
