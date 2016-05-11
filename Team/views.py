# clubs/views.py
from Team.models import PlayerRequest
from .models import Team, PlayerRequest
from Players.models import Player
from django.contrib.auth.models import User

# for I18N
from django.utils.translation import ugettext as _

# TSoD page 98, Class-based views
from django.core.urlresolvers import reverse
# end TSoD
# signals.receiver
from django.db.models import signals

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin
from django.contrib import messages

from Team.forms.team_forms import NewTeamForm
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
        

class TeamListView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, ListView):
    model = Team
    page_title = _("Team List")
    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        this_owner = self.request.user
        teams = Team.objects.filter(owner=this_owner)
        context["team_list"] = teams

        return context



class TeamDetailView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, DetailView):
    model = Team
    page_title = _("Team Detail")

    def get_context_data(self, **kwargs):
        this_team = self.get_object(queryset=None)
        if Team.is_owner(this_team, self.request.user):
            context = super(TeamDetailView, self).get_context_data(**kwargs)
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
            dfpts = 0
            dfptsg = 0
            dgp = 0
            dpyds = 0
            dptd = 0
            dryd = 0
            drtd = 0
            drecyds = 0
            drectd = 0
            dfum = 0
            dsack = 0
            dfr = 0
            dintercept = 0
            dtd = 0
            dsfty =0
            dfg = 0
            dfgmiss = 0
            dxpt = 0

            context["player_request_count"] = len(player_requests)
            context["player_actual_count"] = len(player_list)
            context["player_list"] = player_list
            context["player_request_list"] = player_requests
            if(player_list != None):
                for p in player_list:
                    fpts += p.fpts
                    fptsg += p.fptsg
                    gp += p.gp
                    pyds += p.pyds
                    ptd += p.ptd
                    ryd += p.ryd
                    rtd += p.rtd
                    recyds += p.recyds
                    rectd += p.rectd
                    fum += p.fum
                    sack += p.sack
                    fr += p.fr
                    intercept += p.intercept
                    td += p.td
                    sfty += p.sfty
                    fg += p.fg
                    fgmiss += p.fgmiss
                    xpt += p.xpt
            if(len(player_requests) > 1):
                dfpts = player_requests[0].player.fpts - player_requests[1].player.fpts
                dfptsg = player_requests[0].player.fptsg - player_requests[1].player.fptsg
                dgp = player_requests[0].player.gp - player_requests[1].player.gp
                dpyds = player_requests[0].player.pyds - player_requests[1].player.pyds
                dptd = player_requests[0].player.ptd - player_requests[1].player.ptd
                dryd = player_requests[0].player.ryd - player_requests[1].player.ryd
                drtd = player_requests[0].player.rtd - player_requests[1].player.rtd
                drecyds = player_requests[0].player.recyds - player_requests[1].player.recyds
                drectd = player_requests[0].player.rectd - player_requests[1].player.rectd
                dfum = player_requests[0].player.fum - player_requests[1].player.fum
                dsack = player_requests[0].player.sack - player_requests[1].player.sack
                dfr = player_requests[0].player.fr - player_requests[1].player.fr
                dintercept = player_requests[0].player.intercept - player_requests[1].player.intercept
                dtd = player_requests[0].player.td - player_requests[1].player.td
                dsfty = player_requests[0].player.sfty - player_requests[1].player.sfty
                dfg = player_requests[0].player.fg - player_requests[1].player.fg
                dfgmiss = player_requests[0].player.fgmiss - player_requests[1].player.fgmiss
                dxpt = player_requests[0].player.xpt - player_requests[1].player.xpt


            for p in player_list:
                fpts += p.fpts
                fptsg += p.fptsg
                gp += p.gp
                pyds += p.pyds
                ptd += p.ptd
                ryd += p.ryd
                rtd += p.rtd
                recyds += p.recyds
                rectd += p.rectd
                fum += p.fum
                sack += p.sack
                fr += p.fr
                intercept += p.intercept
                td += p.td
                sfty += p.sfty
                fg += p.fg
                fgmiss += p.fgmiss
                xpt += p.xpt


            # count = 0;

            # acomp = PlayerRequest.objects.filter(teamToJoin=this_team)
            # qcomp = []

            # for p in acomp:
            #     for s in acomp:
            #         if p.player.pk!=s.player.pk:
            #             comp = acomp[1]
            #             comp.player.name = count
            #             comp.player.fpts = p.player.fpts - s.player.fpts
            #             comp.player.fptsg = p.player.fptsg - s.player.fptsg
            #             comp.player.gp = p.player.gp - s.player.gp
            #             comp.player.pyds = p.player.pyds - s.player.pyds
            #             comp.player.ptd = p.player.ptd - s.player.ptd
            #             comp.player.ryd = p.player.ryd - s.player.ryd
            #             comp.player.rtd = p.player.rtd - s.player.rtd
            #             comp.player.recyds = p.player.recyds - s.player.recyds
            #             comp.player.rectd = p.player.rectd - s.player.rectd
            #             comp.player.fum = p.player.fum - s.player.fum
            #             comp.player.sack = p.player.sack - s.player.sack
            #             comp.player.fr = p.player.fr - s.player.fr
            #             comp.player.intercept = p.player.intercept - s.player.intercept
            #             comp.player.td = p.player.td - s.player.td
            #             comp.player.sfty = p.player.sfty - s.player.sfty
            #             comp.player.fg = p.player.fg - s.player.fg
            #             comp.player.fgmiss = p.player.fgmiss - s.player.fgmiss
            #             comp.player.xpt = p.player.xpt - s.player.xpt
            #             qcomp.append(comp)
            #             count = count + 1

    ##                  returns list of comparisons 1v2 1v3...1vn 2v3 2v4...2vn
            # context["comparison_list"]= qcomp
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

            context["dfpts"] = dfpts
            context["dfptsg"] = dfptsg
            context["dgp"] = dgp
            context["dpyds"] = dpyds
            context["dptd"] = dptd
            context["dryd"] = dryd
            context["drtd"] = drtd
            context["drecyds"] = drecyds
            context["drectd"] = drectd
            context["dfum"] = dfum
            context["dsack"] = dsack
            context["dfr"] = dfr
            context["dintercept"] = dintercept
            context["dtd"] = dtd
            context["dsfty"] = dsfty
            context["dfg"] = dfg
            context["dfgmiss"] = dfgmiss
            context["dxpt"] = dxpt
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


# class TeamAndPolicyCreateView(LoginRequiredMixin, TeamActionMixin, NavBarMixin):
#     form_classes = {
#         'newteam': NewTeamForm,
#         'newpolicy': NewTeamPolicyForm,
#     }
#     # the 'templates/' part of the path is implied
#     template_name = 'Team/team_and_policy_form.html'



class TeamCreateView(LoginRequiredMixin, TeamActionMixin, NavBarMixin, CreateView):
    model = Team
    success_msg = _("Team created")
    fields = None
    form_class = NewTeamForm
    page_title = _("Team Create")

    def get_form(self, **kwargs):
        form = super(TeamCreateView, self).get_form(**kwargs)
        form.set_owner(self.request.user)

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
            # PlayerRequest.objects.filter(pk=pk)
            player_request_object = PlayerRequest.objects.get(pk=pk)
            # askingPlayer = player_request_object.requester
            teamToJoin = player_request_object.teamToJoin
            player = Player.objects.get(pk=player_request_object.player.pk)
            teamToJoin.add_player(player)
            player_request_object.delete()
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

def DeletePlayerRequest(request, pk):
    req = PlayerRequest.objects.get(pk=pk)
    team = req.teamToJoin.pk
    req.delete()
    return HttpResponseRedirect(reverse('Team:detail', kwargs={"pk": team}))

def DeleteTeamPlayer(request, team, player):
    team = Team.objects.get(pk=team)
    player = Player.objects.get(pk=player)
    team.delete_player(player)
    return HttpResponseRedirect(reverse('Team:detail', kwargs={"pk": team.pk}))



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

def compareRequestedPlayers(request, playerRequest):
    player = PlayerRequest.objects.get(pk=playerRequest)
    otherPlayers = PlayerRequest.objects.filter(requester=request.user)
    return render(request, 'Team/comparePlayers.html', {"player": player, "others":otherPlayers })

