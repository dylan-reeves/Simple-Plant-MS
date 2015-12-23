from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # example of url /simpleplantms/schedule/
    url(r'^$', login_required(views.IndexView.as_view()), name='schedule-index'),
    # example of url /simpleplantms/schedule/20/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()),
        name='schedule-details'),
    # example of url /simpleplantms/schedule/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        login_required(views.UpdateView.as_view()), name='schedule-update'),
    # example of url /simpleplantms/schedule/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        login_required(views.DeleteView.as_view()), name='schedule-delete'),
    # example of url /simpleplantms/schedule/create/
    url(r'^create/', login_required(views.CreateView.as_view()),
        name='schedule-create'),

]
