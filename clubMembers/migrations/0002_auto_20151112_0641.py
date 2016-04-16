# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clubMembers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubmember',
            name='phone',
        ),
        migrations.AlterField(
            model_name='clubmember',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\(\\d{3}\\)[ -]\\d{3}[ -]\\d{4}', message=b'Phone must be (###) 555 1212 or ### 555 1212; you can use dashes instead of spaces')]),
        ),
    ]
