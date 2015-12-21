from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # example of url /simpleplantms/maintjobs/
    url(r'^$', login_required(views.IndexView.as_view()), name='maintjobs-index'),
    # example of url /simpleplantms/maintjobs/20/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()),
        name='miantjobs-details'),
    # example of url /simpleplantms/maintjobs/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        login_required(views.UpdateView.as_view()), name='maintjobs-update'),
    # example of url /simpleplantms/maintjobs/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        login_required(views.DeleteView.as_view()), name='maintjobs-delete'),
    # example of url /simpleplantms/maintjobs/create/
    url(r'^create/', login_required(views.CreateView.as_view()),
        name='maintjobs-create'),
]
