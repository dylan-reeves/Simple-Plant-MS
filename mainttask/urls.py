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
    # example of url /simpleplantms/maintjobs/34/copy/
    url(r'^(?P<pk>[0-9]+)/copy/$',
        views.CopyView, name='maintjobs-copy'),
    # example of url to add maintenance job - task /simpleplantms/maintjobs/5/addtask
    url(r'^(?P<pk>[0-9]+)/addtask/$',
        login_required(views.AddTaskView.as_view()), name='maintjobs-addtask'),
    #exmaple of url to update maintennace job - task /simpleplantms/maintjobs/2/updatetask
    url(r'^(?P<pk>[0-9]+)/updatetask/$',
        login_required(views.UpdateTaskView.as_view()), name='maintjobs-updatetask'),
    #exmaple of url to update maintennace job - task /simpleplantms/maintjobs/2/deletetask
    url(r'^(?P<pk>[0-9]+)/deletetask/$',
        login_required(views.DeleteTaskView.as_view()), name='maintjobs-deletetask'),
    #example of url to ask if want to add another task /simpleplantms/maintjobs/3/addanothertask
    url(r'^(?P<pk>[0-9]+)/addanothertask/$',
        login_required(views.AddAnotherTaskView.as_view()), name='maintjobs-addanothertask'),
]
