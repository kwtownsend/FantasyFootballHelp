from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# from clubs.models import Club
import datetime
from django.utils import timezone

from django.contrib import admin
from django.forms import ModelForm
from Players.models import Player



class Team(models.Model):
    owner = models.ForeignKey(User)
    public = models.BooleanField(help_text='If checked, people can ask to join your club', default=True)
    # visible = models.BooleanField(help_text='If checked, people can see your club', default=True)
    max_players = models.PositiveSmallIntegerField(default=16, help_text='Maximum players allowed on this team')
    # lending_days = models.PositiveSmallIntegerField(default=21, help_text='Number of days for borrowing/lending thingys')
    players = models.ForeignKey(Player)

    # add other policies here
    #
class PlayerRequest(models.Model):
    requester = models.ForeignKey(User)
    teamToJoin = models.ForeignKey(Team)
    # request_date = models.DateField(default=timezone.now)
    # reasonMessage = models.CharField(max_length=200, help_text="Why do you want to join this club?")

