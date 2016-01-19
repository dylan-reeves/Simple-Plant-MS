from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # example of url /simpleplantms/maintenance/
    url(r'^$', login_required(views.IndexView.as_view()), name='maintenance-index'),
    # example of url /simpleplantms/maintenance/20/execute
    url(r'^(?P<pk>[0-9]+)/execute/$', views.ExecuteView,
        name='execute-maintenance'),
    # example of url /simpleplantms/equipment/34/update/
    #url(r'^(?P<pk>[0-9]+)/update/$',
    #    login_required(views.UpdateView.as_view()), name='equipment-update'),
    # example of url /simpleplantms/equipment/34/delete/
    #url(r'^(?P<pk>[0-9]+)/delete/$',
    #    login_required(views.DeleteView.as_view()), name='equipment-delete'),
    # example of url /simpleplantms/equipment/create/
    #url(r'^create/', login_required(views.CreateView.as_view()),
    #    name='equipment-create'),
    #example of url /simpleplantms/equipment/6/addschedule
    #url(r'^(?P<pk>[0-9]+)/addschedule/$',
    #    login_required(views.AddScheduleView.as_view()), name='equipment-schedule-add'),
    #example of url /simpleplantms/equipment/3/updateschedule
    #url(r'^(?P<pk>[0-9]+)/updateschedule/$',
    #    login_required(views.UpdateScheduleView.as_view()), name='equipment-schedule-update'),
    #example of url /simpleplantms/equipment/7/deleteschedule
    #url(r'^(?P<pk>[0-9]+)/deleteschedule/$',
    #    login_required(views.DeleteScheduleView.as_view()), name='equipment-schedule-delete'),
]
