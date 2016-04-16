# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clubMembers', '0003_memberrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmember',
            name='member_zip',
            field=models.CharField(default='90001', max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}$', message=b'5-digit Zip Code only')]),
            preserve_default=False,
        ),
    ]
