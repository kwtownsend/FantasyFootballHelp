from django.shortcuts import render
from .models import ClubMember

# for I18N
from django.utils.translation import ugettext as _

# TSoD page 98, Class-based views
from django.core.urlresolvers import reverse
# end TSoD
# signals.receiver
from django.db.models import signals

from django.http import Http404

from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from braces.views import LoginRequiredMixin
from django.contrib import messages

from helpers.navbar_helpers import NavBarMixin
from django.contrib import messages
from django.contrib.auth.models import User


class ClubMemberMixin(object):
    """
    Only certain people are authorized to view, update ClubMember info.
    The member who owns the info,
    and a club leader who wants to allow them to join.
    Maybe a simple view for other people in clubs they're in
    """
    def get_context_data(self, **kwargs):
        context = super(ClubMemberMixin, self).get_context_data(**kwargs)
        context["userInfo"] = User.objects.get(pk=self.kwargs["pk"])
        return context




class ClubMemberListView(LoginRequiredMixin, NavBarMixin, ListView):
    """
    This can be a stats page.
    Maybe show how many members in each zip code or some basic member statistics.
    Show graph of how many thingys per member, whatever. Something.
    Not needed at this time, really.
    No personal info, though.
    """
    model = ClubMember
    page_title = _("Club Member List")


class ClubMemberDetailView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
    model = ClubMember
    page_title = _("Club Member Detail")



class ClubMemberUpdateView(LoginRequiredMixin, NavBarMixin, UpdateView):
    model = ClubMember
    page_title = _("Club Member Update View")


class ClubMemberResultsView(LoginRequiredMixin, NavBarMixin,DetailView):
    model = ClubMember
    page_title = _("Club Member Results View")


class ClubMemberDeleteView(LoginRequiredMixin, NavBarMixin, DeleteView):
    model = ClubMember
    page_title = _("Club Member Delete View")


class ClubMemberInfoView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
    """
    This is to look at info about another member.
    This view needs to find out the member relationship:
      (Self)    self -> use DetailView
      (Club)    in same club -> public + club-level info
      (PndM)    in club that this pk wants to join -> public + club-prospective info
      (ClbL)    club leader of club pk is in -> public + club-level info
      (PndL)    club leader of club pk wants to join -> public + club-prospective + (whatever) info
      (User)    world+dog -> public-level info only
      (Anon)    anonymous user -> none
    Since this view has a lot more checks, give it a different url,
    since it'll take more processing to go through all the checks.
    We can complete the (Self) and (PndL) first, and give everyone else -> none
    """
    model = ClubMember
    page_title = _("Club Member Detail")


class ClubMemberFirstTimeView(LoginRequiredMixin, ClubMemberMixin, NavBarMixin, DetailView):
    """
    A new member on the site will be sent here after registering.
    They are automatically logged in, and this is the method called.
    Put some ajax happy stuff in here, or a couple tutorial videos.
    Tell them to complete their user profile and join or start a club.
    """
    model = ClubMember
    page_title = _("Club Member First Time")


