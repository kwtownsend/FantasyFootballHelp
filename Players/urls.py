from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
	url(
        regex=r"^(?P<pk>\d+)$",
        view=views.PlayerDetailView.as_view(),
        name="detail")
        ]

# urlpatterns = [
#     url(
#         regex=r"^$",
#         view=views.ClubMemberListView.as_view(),
#         name="list"
#     ),
#     url(
#         regex=r"^(?P<pk>\d+)$",
#         view=views.ClubMemberDetailView.as_view(),
#         name="detail"
#     ),
#     url(
#         regex=r"info/^(?P<pk>\d+)$",
#         view=views.ClubMemberInfoView.as_view(),
#         name="info"
#     ),
#     url(
#         regex=r"^welcome/(?P<pk>\d+)$",
#         view=views.ClubMemberFirstTimeView.as_view(),
#         name="first_time"
#     ),
#     url(
#         regex=r"^results/(?P<pk>\d+)$",
#         view=views.ClubMemberResultsView.as_view(),
#         name="results"
#     ),
#     url(
#         regex=r"^update/(?P<pk>\d+)$",
#         view=views.ClubMemberUpdateView.as_view(),
#         name="update"
#     ),
#     url(
#         regex=r"^delete/(?P<pk>\d+)$",
#         view=views.ClubMemberDeleteView.as_view(),
#         name="delete"
#     ),
# ]
