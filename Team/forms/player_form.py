from django.forms import ModelForm

from Team.models import Team, PlayerRequest

from django.http import Http404
import datetime




class newPlayerForm(ModelForm):
    class Meta:
        model = PlayerRequest
        fields = ["reasonMessage"]

    _requester = None
    _owner = None
    _teamToJoin = None
    _playerToJoin = None

    def set_requester(self, requester):
        self._requester = requester

    def set_owner(self, requester):
        self._owner = owner

    def set_teamToJoin(self, teamToJoin):
        self._teamToJoin = teamToJoin



    def save(self, *args, **kwargs):
        # if self._policy:
        #     self.instance.policies = self._policy
        # else:
        #     return Http404("something is wrong")

        # self.instance.request_date = datetime.datetime.now()
        self.instance.requester = self._requester
        # playerWanted = Player.objects.get(pk=)
        teamWanted = Team.objects.get(pk=self._teamToJoin)
        self.instance.teamToJoin = teamWanted
        # self.instance.clubToJoin = self._clubToJoin
        resp = super(newPlayerForm, self).save(*args, **kwargs)
        return resp
