from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # example of url /simpleplantms/departments/
    url(r'^$', login_required(views.IndexView.as_view()), name='departments-index'),
    # example of url /simpleplantms/departments/20/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()),
        name='departments-details'),
    # example of url /simpleplantms/departments/34/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        login_required(views.UpdateView.as_view()), name='departments-update'),
    # example of url /simpleplantms/departments/34/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        login_required(views.DeleteView.as_view()), name='departments-delete'),
    # example of url /simpleplantms/departments/create/
    url(r'^create/', login_required(views.CreateView.as_view()),
        name='departments-create'),
]
