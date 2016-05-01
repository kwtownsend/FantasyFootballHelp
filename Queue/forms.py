from django.forms import ModelForm

from Team.models import Team
from Queue.models import Queue

from django.http import Http404
import datetime


class NewTeamPolicyForm(ModelForm):
    # name = models.CharField(max_length=20, help_text='Club name')
    # description = models.CharField(max_length=180, help_text='Club description')
    # zipcode = models.CharField(max_length=5)
    # add_date = models.DateField(default=timezone.now)
    # members = models.ManyToManyField(User)
    # policies = models.ForeignKey('clubPolicies.ClubPolicy')
    class Meta:
        model = Queue
        fields = ['public']



