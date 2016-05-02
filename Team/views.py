# clubs/views.py
from Team.models import PlayerRequest
from .models import Team, PlayerRequest
from Queue.models import Queue
from django.contrib.auth.models import User

# for I18N
from django.utils.translation import ugettext as _

# TSoD page 98, Class-based views
from django.core.urlresolvers import reverse
# end TSoD
# signals.receiver
from django.db.models import signals

from django.http import Http404, HttpResponseRedirect

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib import messages

from Team.forms.team_forms import NewTeamForm
from Team.forms.queue_forms import NewTeamPolicyForm
from Team.forms.player_form import newPlayerForm
from Team.forms.playerrequestform import newPlayerRequest

# from Team.forms.member_form import newMemberForm
from helpers.navbar_helpers import NavBarMixin
from django.contrib import messages


class TeamActionMixin(object):
    
    fields = ('name')
    
    @property
    def success_msg(self):
        return NotImplemented

    @staticmethod
    def is_member_current_user(self, member):
        """
        Is the current user the member being looked at
        :param self:
        :return:
        """
        pass
        

class TeamListView(NavBarMixin, ListView):
    model = Team
    page_title = _("Club List")


class TeamDetailView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, DetailView):
    model = Team
    page_title = _("Club Detail")

    def get_context_data(self, **kwargs):
        # world+dog context data goes here
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        # self.navBar_context(context)
        # context["page_title"] = _("Club Detail")
        # context["available_thingys"] = self.thingys_available()
        this_team = self.get_object(queryset=None)
        # player = self.get_object(queryset=None)
        player_list = this_team.players.all()
        player_requests = PlayerRequest.objects.filter(teamToJoin=this_team)
        fpts = 0
        fptsg = 0
        gp = 0
        pyds = 0
        ptd = 0
        ryd = 0
        rtd = 0
        recyds = 0
        rectd = 0
        fum = 0
        sack = 0
        fr = 0
        intercept = 0
        td = 0
        sfty =0
        fg = 0
        fgmiss = 0
        xpt = 0
        context["player_request_count"] = len(player_requests)
        context["player_actual_count"] = len(player_list)
        context["player_list"] = player_list
        context["player_request_list"] = player_requests
        for p in player_requests:
            fpts += p.player.fpts
            fptsg += p.player.fptsg
            gp += p.player.gp
            pyds += p.player.pyds
            ptd += p.player.ptd
            ryd += p.player.ryd
            rtd += p.player.rtd
            recyds += p.player.recyds
            rectd += p.player.rectd
            fum += p.player.fum
            sack += p.player.sack
            fr += p.player.fr
            intercept += p.player.intercept
            td += p.player.td
            sfty += p.player.sfty
            fg += p.player.fg
            fgmiss += p.player.fgmiss
            xpt += xpt
        context["fpts"] = fpts
        context["fptsg"] = fptsg
        context["gp"] = gp
        context["pyds"] = pyds
        context["ptd"] = ptd
        context["ryd"] = ryd
        context["rtd"] = rtd
        context["recyds"] = recyds
        context["rectd"] = rectd
        context["fum"] = fum
        context["sack"] = sack
        context["fr"] = fr
        context["intercept"] = intercept
        context["td"] = td
        context["sfty"] = sfty
        context["fg"] = fg
        context["fgmiss"] = fgmiss
        context["xpt"] = xpt
        # all_entries = Team.players.all()
        # context["top_panel_name"] = "Members"
        # context["bottom_panel_name"] = "Request Membership"
        # context["member_count"] = len(player_list)
        # if Team.is_owner(this_team, self.request.user):
        #     # member specific context data goes here
        #     context["bottom_panel_name"] = "Membership Requests"
        # context["player"] = True


        #     context["member_requests"] = this_team.player_requests_list()
        #     if Team.is_owner(this_team, self.request.user):
        #         context["owner"] = True

        # if Team.is_owner(this_team, self.request.user):
        #     # leader specific context data goes here
        #     pass
        return context


class TeamAndPolicyCreateView(LoginRequiredMixin, TeamActionMixin, NavBarMixin):
    form_classes = {
        'newteam': NewTeamForm,
        'newpolicy': NewTeamPolicyForm,
    }
    # the 'templates/' part of the path is implied
    template_name = 'Team/team_and_policy_form.html'



class TeamCreateView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, CreateView):
    model = Team
    success_msg = _("Team created")
    fields = None
    form_class = NewTeamForm
    page_title = _("Team Create")

    def get_form(self, **kwargs):
        form = super(TeamCreateView, self).get_form(**kwargs)
        # form.set_leader(self.request.user)
        # form.set_policy(Queue.objects.create(public=True, leader=self.request.user))
        # form.set_owner(self.request.user)
        # print("pk of policy object is " + str(NewTeamForm.get_policy))
        return form

    def post(self, request, *args, **kwargs):
        # self.object = None
        return super(CreateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("Team:detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        print("the passed-in 'self' object is a : " + repr(type(self)))
        print("the passed-in 'form' object is a : " + repr(type(form)))
        resp = super(TeamActionMixin, self).form_valid(form)
        # self.object.players.add(self.request.user)
        messages.info(self.request, self.success_msg)
        return resp

    # def get_context_data(self, **kwargs):
    #     # world+dog context data goes here
    #     context = super(ClubDetailView, self).get_context_data(**kwargs)
    #     self.navBar_context(context)
    #     context["page_title"] = _("Club Detail")
    #     # context["available_thingys"] = self.thingys_available()
    #     return context



class TeamResultsView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, DetailView):
    """
    Detail view after create/update of club.
    """
    model = Team
    page_title = _("Club Results")


class TeamUpdateView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, UpdateView):
    model = Team
    success_msg = _("Team updated")
    page_title = _("Team Update")

    def get_success_url(self):
        return reverse("Team:detail", kwargs={"pk": self.object.pk})


class TeamDeleteView(LoginRequiredMixin, TeamActionMixin, DeleteView):
    model = Team
    page_title = _("Team Delete")

    def get_object(self, queryset=None):
        """Hook to ensure club leader guy is request.user"""
        obj = super(TeamDeleteView, self).get_object()
        # leaderGuy = obj.policies.owner
        if not leaderGuy == self.request.user:
            raise Http404(_("You're not the owner of this team, so fuck off."))
        return obj
        
    def get_success_url(self):
        return reverse("Team:list")

###############################################################################
# Club Member stuff

class PlayerActionMixin(object):

    # fields = ('reasonMessage',)

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        print("the passed-in 'self' object is a : " + repr(type(self)))
        print("the passed-in 'form' object is a : " + repr(type(form)))
        resp = super(PlayerActionMixin, self).form_valid(form)
        # self.object.members.add(self.request.user)
        messages.info(self.request, self.success_msg)
        return resp



# class ClubAddMemberView(LoginRequiredMixin, ClubMemberActionMixin, NavBarMixin, DetailView):
#     """
#     Page where authorized user (leader?) can add members.
#     This may be unnedded, or something like "ClubInviteMembersView".
#     Maybe this is the results page for a member add to a club?
#     """
#     model = MemberRequest
#     page_title = _("Club Add Member")
#     success_msg= _("Member added to club")


#     # TODO: Anyone can approve the member join. They just need to know the url pattern.

#     def get(self, request, pk=None, *args, **kwargs):
#         if pk:
#             member_request_object = MemberRequest.objects.get(pk=pk)
#             askingMember = member_request_object.requester
#             clubToJoin = member_request_object.clubToJoin
#             clubToJoin.add_member(askingMember)
#             member_request_object.delete()

class TeamAddPlayerView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, DetailView):
    """
    Page where authorized user (leader?) can add members.
    This may be unnedded, or something like "ClubInviteMembersView".
    Maybe this is the results page for a member add to a club?
    """
    model = PlayerRequest
    page_title = _("Club Add Member")
    success_msg= _("Member added to club")


    # TODO: Anyone can approve the member join. They just need to know the url pattern.

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            player_request_object = PlayerRequest.objects.get(pk=Player.pk)
            # askingPlayer = player_request_object.requester
            teamToJoin = member_request_object.teamToJoin
            teamToJoin.add_player(player_request_object)
            member_request_object.delete()
            return HttpResponseRedirect(reverse('Team:detail', kwargs={"pk": teamToJoin.pk}))

# class TeamAddPlayerView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, DetailView):
#     """
#     Page where authorized user (leader?) can add members.
#     This may be unnedded, or something like "ClubInviteMembersView".
#     Maybe this is the results page for a member add to a club?
#     """
#     model = PlayerRequest
#     page_title = _("Club Add Member")
#     success_msg= _("Member added to club")



#     def get(self, request, pk=None, *args, **kwargs):
#         # if pk:
#             player_request = PlayerRequest.objects.get(pk=pk)
#             teamToJoin = player_request.teamToJoin
#             askingUser = self.request.user
            
#             player_requests = PlayerRequest.objects.filter(teamToJoin=this_team)

#             teamToJoin.add_player(player_request.player)

#             player_request_object.delete()
#             return HttpResponseRedirect(reverse('Team:detail', kwargs={"pk": teamToJoin.pk}))
            # else:
            #     return HttpResponseRedirect(redirect_to=reverse('welcome'))

class TeamRemovePlayerView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, DetailView):
    model = PlayerRequest
    page_title = _("Club Add Member")
    success_msg= _("Member added to club")
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            player_request_object = PlayerRequest.objects.get(pk=3)
            # teamToJoin = player_request_object.teamToJoin
            askingUser = self.request.user
            player_request_object.remove(pk=pk)
            # player_requests = PlayerRequest.objects.filter(teamToJoin=this_team)

            # teamToJoin.add_player(player_request_object.player)

            player_request_object.delete()
            return HttpResponseRedirect(reverse('Team:detail', kwargs={"pk": teamToJoin.pk}))


class TeamAskJoinView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, CreateView):
    """
    A member of the site has asked to become
    a member of a specific club.
    This request should be sent to the club leader.
    """
    # template_name = "clubs/requestJoin.html"
    # fields = ["teamToJoin"]
    model = PlayerRequest
    form_class = newPlayerRequest
    success_msg = _("Request sent to Club Leader")
    page_title = _("Club Ask to Join")


    # fields = ['reasonMessage', ]
    def get_form(self, **kwargs):
        form = super(TeamAskJoinView, self).get_form(**kwargs)
        form.set_requester(self.request.user)
        # the_team = Team.objects.get(pk=1)
        # form.set_teamToJoin()
        print(self.kwargs['pk'])
        print(('checking'))
        # if 'pk' in kwargs:
        #     print('plswork')
        #     print(kwargs.get('pk'))
        form.set_player(self.kwargs['pk'])
        # how can I get the pk of the current club from the url, or from somewhere?
        # form.set_teamToJoin(self.kwargs['pk'])
        return form

    def get_success_url(self):
        return reverse('Team:confirmAskJoin', kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PlayerActionMixin, self).form_valid(form)



class TeamConfirmAskJoinView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, DetailView):
    """
    Confirmation page for person who's asked
    to join a club
    """
    model = PlayerRequest
    page_title = _("Club Confirm ask to join")


# class ClubEditMemberView(LoginRequiredMixin, ClubMemberActionMixin, DetailView):
#     """
#     Allows a club leader to edit a member? This is just wrong.
#     Maybe I was thinking that Member info needed to be edited
#     through the club views. It's a DetailView. Clarify.
#     """
#     model = Club
#     page_title = _("Club Edit")



