from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

from django.contrib import admin
from django.forms import ModelForm


class Queue(models.Model):
    leader = models.ForeignKey(User)
    public = models.BooleanField(help_text='If checked, people can ask to join your club', default=True)
    # visible = models.BooleanField(help_text='If checked, people can see your club', default=True)
    max_players = models.PositiveSmallIntegerField(default=12, help_text='Maximum number of members allowed in this club')
    # lending_days = models.PositiveSmallIntegerField(default=21, help_text='Number of days for borrowing/lending thingys')
    # add other policies here
    # 