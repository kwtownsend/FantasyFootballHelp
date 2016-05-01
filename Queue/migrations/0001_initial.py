# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.BooleanField(default=True, help_text=b'If checked, people can ask to join your club')),
                ('max_players', models.PositiveSmallIntegerField(default=12, help_text=b'Maximum number of members allowed in this club')),
                ('leader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
