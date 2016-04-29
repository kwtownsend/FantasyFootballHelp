from django.utils.translation import ugettext as _
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from braces.views import LoginRequiredMixin
from django.shortcuts import render_to_response
from django.template import RequestContext

# TSoD page 98, Class-based views
from django.core.urlresolvers import reverse
# end TSoD
from django.http import Http404, HttpResponseRedirect
# from clubs.models import Club
from django.contrib.auth.models import User
# from clubMembers.models import ClubMember

from .models import Player  #player class
# from thingys.forms.thingy_forms import new_thingy_form

from helpers.navbar_helpers import NavBarMixin

class PlayerActionMixin(object):
    fields = ('name', 'pos', 'fpts', 'fptsg', 'gp', 'pyds', 'ptd', 'ryd', 'rtd', 'recyds', 'rectd', 'fum', 'sack', 
        'fr', 'intercept', 'td', 'sfty', 'fg', 'fgmiss', 'xpt')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PlayerActionMixin, self).form_valid(form)

    # def is_owner(self, thingy):
    #     if thingy.owner == self.request.user:
    #         return True
        return False


class PlayerDetailView(LoginRequiredMixin, PlayerActionMixin, NavBarMixin, DetailView):
    model = Player
    template_name = "Players/player_detail.html"
    page_title = _("Available Player Detail")

    def get(self, request, *args, **kwargs):
        player = self.get_object(queryset=None)
        # object_owner_member = ClubMember.objects.get(member=thingy.owner)
        # requesting_member = ClubMember.objects.get(member=request.user)
        # relationship = user_relation(thingy.owner, request.user)
        # print(relationship)
        # if relationship == "clubRelated":
        return super(PlayerDetailView, self).get(self, request, *args, **kwargs)
        # if relationship == "notRelated":
        #     print(" *******\nuser is trying to access non members thingys through url tweaking")
        #     print(request.user.username)
        #     print("is the user trying it\n *******")
        #     return HttpResponseRedirect(redirect_to=reverse('welcome'))


class PlayerSearchView(NavBarMixin, ListView):
    model = Player
    page_title = _("Thingy Search View")


# class PlayerDetailView(LoginRequiredMixin, ThingyActionMixin, NavBarMixin, DetailView):
#     model = Player
#     page_title = _("Your Thingys Detail")

#     def get_context_data(self, **kwargs):
#         context = super(PlayerDetailView, self).get_context_data(**kwargs)
#         this_Player = self.get_object()
#         # relationship = user_relation(this_thingy.owner, self.request.user)
#         # if relationship == "selfRelated":
#             # context["selfRelated"] = True
#         context["requested"], context["ask_object_lender"] = ask_borrow_object_for_owner(this_thingy, self.request.user)
#             # add more owner-specific info
#         # elif relationship == "clubRelated":
#             # context["clubRelated"] = True
#             # context["already_requested"], context["ask_objects"] = thingy_requested_by_user(this_thingy, self.request.user)
#             # context["request_accepted"] = thingy_request_accepted_for_user(this_thingy, self.request.user)
#             # context["available"] = thingy_available_for_request(this_thingy)
#             # add more club buddy specific info
#         # elif relationship == "pendingMemberMember":
#             # context["pendingMemberMember"] = True
#             # add more info for a pending member to view a current member thingy
#         # elif relationship == "memberPendingMember":
#             # context["memberPendingMember"] = True
#             # maybe a member wants to check out what kind of thingys
#             # a requesting member might have
#         # else:
#             # context["notRelated"] = True
#             # this person is not related to thingy owner in any way.
#             # give basic info
#         return context


# @staff_member_required
# def import(request):
#     if request.method == "POST":
#         form = DataInput(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             success = True
#             context = {"form": form, "success": success}
#             return render_to_response("imported.html", context,
#             context_instance=RequestContext(request))
#     else:
#         form = DataInput()        
#         context = {"form": form}
#         return render_to_response("imported.html", context,
#         context_instance=RequestContext(request)) 



# class ClubMemberMixin(object):
#     """
#     Only certain people are authorized to view, update ClubMember info.
#     The member who owns the info,
#     and a club leader who wants to allow them to join.
#     Maybe a simple view for other people in clubs they're in
#     """
#     def get_context_data(self, **kwargs):
#         context = super(ClubMemberMixin, self).get_context_data(**kwargs)
#         context["userInfo"] = User.objects.get(pk=self.kwargs["pk"])
#         return context




# class ClubMemberListView(LoginRequiredMixin, NavBarMixin, ListView):
#     """
#     This can be a stats page.
#     Maybe show how many members in each zip code or some basic member statistics.
#     Show graph of how many thingys per member, whatever. Something.
#     Not needed at this time, really.
#     No personal info, though.
#     """
#     model = ClubMember
#     page_title = _("Club Member List")


# class ClubMemberDetailView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
#     model = ClubMember
#     page_title = _("Club Member Detail")



# class ClubMemberUpdateView(LoginRequiredMixin, NavBarMixin, UpdateView):
#     model = ClubMember
#     page_title = _("Club Member Update View")


# class ClubMemberResultsView(LoginRequiredMixin, NavBarMixin,DetailView):
#     model = ClubMember
#     page_title = _("Club Member Results View")


# class ClubMemberDeleteView(LoginRequiredMixin, NavBarMixin, DeleteView):
#     model = ClubMember
#     page_title = _("Club Member Delete View")


# class ClubMemberInfoView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
#     """
#     This is to look at info about another member.
#     This view needs to find out the member relationship:
#       (Self)    self -> use DetailView
#       (Club)    in same club -> public + club-level info
#       (PndM)    in club that this pk wants to join -> public + club-prospective info
#       (ClbL)    club leader of club pk is in -> public + club-level info
#       (PndL)    club leader of club pk wants to join -> public + club-prospective + (whatever) info
#       (User)    world+dog -> public-level info only
#       (Anon)    anonymous user -> none
#     Since this view has a lot more checks, give it a different url,
#     since it'll take more processing to go through all the checks.
#     We can complete the (Self) and (PndL) first, and give everyone else -> none
#     """
#     model = ClubMember
#     page_title = _("Club Member Detail")


# class ClubMemberFirstTimeView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
#     """
#     A new member on the site will be sent here after registering.
#     They are automatically logged in, and this is the method called.
#     Put some ajax happy stuff in here, or a couple tutorial videos.
#     Tell them to complete their user profile and join or start a club.
#     """
#     model = ClubMember
#     page_title = _("Club Member First Time")


