# clubs urls.py
from django.conf.urls import patterns, include, url
from . import views


# TODO: I want to standardize namespace names to all lowercase
# e.g. confirmAskJoin > confirmaskjoin,
#      editMember > editMember
# TODO: addMembers is plural. singularize it
# were we really going to add members en masse?


urlpatterns = [
    url(
        regex=r"^$",
        view=views.TeamListView.as_view(),
        name="list"
    ),
    # url(
    #     regex=r"^new$",
    #     view=views.ClubAndPolicyCreateView.as_view(),
    #     name="new"
    # ),
    url(
        regex=r"^new$",
        view=views.TeamCreateView.as_view(),
        name="new"
    ),
    url(
        regex=r"^(?P<pk>\d+)$",
        view=views.TeamDetailView.as_view(),
        name="detail"
    ),
    # url(
    #     regex=r"^join/(?P<pk>\d+)$",
    #     view=views.ClubAskJoinView.as_view(),
    #     name="askjoin"
    # ),
    # url(
    #     regex=r"^confirm/(?P<pk>\d+)$",
    #     view=views.ClubConfirmAskJoinView.as_view(),
    #     name="confirmAskJoin"
    # ),
   url(
        regex=r"^addmember/(?P<pk>\d+)$",
        view=views.TeamAddPlayerView.as_view(),
        name="addmember"
    ),
   # url(
   #      regex=r"^declinemember/(?P<pk>\d+)$",
   #      view=views.ClubDeclineMemberView.as_view(),
   #      name="declinemember"
   #  ),
   # url(
   #      regex=r"^editmember/(?P<pk>\d+)$",
   #      view=views.ClubEditMemberView.as_view(),
   #      name="editMember"
   #  ),
    url(
        regex=r"^results/(?P<pk>\d+)$",
        view=views.TeamResultsView.as_view(),
        name="result"
    ),
    url(
        regex=r"^update/(?P<pk>\d+)$",
        view=views.TeamUpdateView.as_view(),
        name="update"
    ),
    url(
        regex=r"^delete/(?P<pk>\d+)$",
        view=views.TeamDeleteView.as_view(),
        name="delete"
    ),
]
