from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # example of url /simpleplantms/sites/
    url(r'^$', login_required(views.IndexView.as_view()), name='sites-index'),
    # example of url /simpleplantms/sites/20/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()),
        name='sites-details'),
    # example of url /simpleplantms/sites/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        login_required(views.UpdateView.as_view()), name='sites-update'),
    # example of url /simpleplantms/sites/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        login_required(views.DeleteView.as_view()), name='sites-delete'),
    # example of url /simpleplantms/sites/create/
    url(r'^create/', login_required(views.CreateView.as_view()), name='sites-create'),
]
