# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reasonMessage', models.CharField(help_text=b'Why do you want to join this club?', max_length=200)),
                ('player', models.ForeignKey(default=1, to='Players.Player')),
                ('requester', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(to='Players.Player')),
            ],
        ),
        migrations.AddField(
            model_name='playerrequest',
            name='teamToJoin',
            field=models.ForeignKey(verbose_name=b'Team Name', to='Team.Team'),
        ),
    ]
