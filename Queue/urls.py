# clubPolicies urls.py
from django.conf.urls import patterns, include, url
from . import views



urlpatterns = [
    url(
        regex=r"^$",
        view=views.PolicyListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^new$",
        view=views.PolicyCreateView.as_view(),
        name="new"
    ),
    url(
        regex=r"^(?P<pk>\d+)$",
        view=views.PolicyDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^results/(?P<pk>\d+)$",
        view=views.PolicyResultsView.as_view(),
        name="result"
    ),
    url(
        regex=r"^update/(?P<pk>\d+)$",
        view=views.PolicyUpdateView.as_view(),
        name="update"
    ),
    url(
        regex=r"^delete/(?P<pk>\d+)$",
        view=views.PolicyDeleteView.as_view(),
        name="delete"
    ),
]
