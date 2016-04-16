# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubMembers', '0002_auto_20151112_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('rating_date', models.DateField()),
                ('rated_by', models.ForeignKey(related_name='member_related', to=settings.AUTH_USER_MODEL)),
                ('target_member', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
